"""Convert study materials (PDF, DOCX, PPTX, TXT/MD/VTT/SRT) into plain-text files in a cache folder.

Why: reading a whole slide deck or transcript into the conversation bloats the context window.
Converting once lets Claude grep the cache and read only the slices it needs, in this session
and in later ones.

Usage:
    python extract_text.py <cache_dir> <file_or_folder> [<file_or_folder> ...]

- Folders are walked recursively.
- A file is re-converted only if it changed since the last run (mtime check).
- DOCX output keeps headings (#), bold runs (**...**) and tables (| a | b |), so the
  cache can also be used to study the user's note-taking style.
- PDF output marks each page as "=== [page N] ===" so slide numbers can be cited.
- Prints one line per file: <status> <chars> <cache path>
"""

import os
import sys

SUPPORTED = {".pdf", ".docx", ".pptx", ".txt", ".md", ".vtt", ".srt"}


def pdf_to_text(path):
    try:
        import pymupdf  # type: ignore
    except ImportError:
        try:
            import fitz as pymupdf  # type: ignore
        except ImportError:
            pymupdf = None
    pages = []
    if pymupdf is not None:
        with pymupdf.open(path) as doc:
            for i, page in enumerate(doc, 1):
                pages.append(f"=== [page {i}] ===\n{page.get_text().strip()}")
    else:
        from pypdf import PdfReader  # type: ignore

        for i, page in enumerate(PdfReader(path).pages, 1):
            pages.append(f"=== [page {i}] ===\n{(page.extract_text() or '').strip()}")
    return "\n\n".join(pages)


def _runs_to_text(paragraph):
    out = []
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
        if run.bold and text.strip():
            lead = text[: len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            text = f"{lead}**{text.strip()}**{trail}"
        out.append(text)
    joined = "".join(out)
    return joined if joined.strip() else paragraph.text


def docx_to_text(path):
    import docx  # type: ignore
    from docx.table import Table  # type: ignore
    from docx.text.paragraph import Paragraph  # type: ignore

    d = docx.Document(path)
    lines = []
    for child in d.element.body.iterchildren():
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "p":
            p = Paragraph(child, d)
            if not p.text.strip():
                continue
            style = (p.style.name if p.style is not None else "") or ""
            text = _runs_to_text(p)
            if style.startswith("Heading"):
                level = style.replace("Heading", "").strip()
                level = int(level) if level.isdigit() else 1
                lines.append(f"{'#' * level} {p.text.strip()}")
            elif style == "Title":
                lines.append(f"# [TITLE] {p.text.strip()}")
            elif "List" in style:
                lines.append(f"- {text}")
            else:
                lines.append(text)
        elif tag == "tbl":
            t = Table(child, d)
            lines.append("[TABLE]")
            for row in t.rows:
                cells = [c.text.replace("\n", " / ").strip() for c in row.cells]
                lines.append("| " + " | ".join(cells) + " |")
            lines.append("[/TABLE]")
    return "\n".join(lines)


def pptx_to_text(path):
    try:
        from pptx import Presentation  # type: ignore
    except ImportError:
        return "[python-pptx not installed: run `pip install python-pptx`, or export the deck to PDF]"
    slides = []
    for i, slide in enumerate(Presentation(path).slides, 1):
        texts = [s.text_frame.text for s in slide.shapes if getattr(s, "has_text_frame", False)]
        notes = ""
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
        body = "\n".join(t for t in texts if t.strip())
        if notes:
            body += f"\n[speaker notes] {notes}"
        slides.append(f"=== [slide {i}] ===\n{body}")
    return "\n\n".join(slides)


def plain_to_text(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


CONVERTERS = {
    ".pdf": pdf_to_text,
    ".docx": docx_to_text,
    ".pptx": pptx_to_text,
}


def cache_name(path):
    # Flatten the path's last two components so files with the same name in different
    # folders don't collide, e.g. "Lecture 1/transcript.pdf" -> "Lecture 1__transcript.pdf.txt"
    parent = os.path.basename(os.path.dirname(os.path.abspath(path)))
    return f"{parent}__{os.path.basename(path)}.txt"


def iter_files(target):
    if os.path.isfile(target):
        yield target
        return
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "_study_cache"]
        for name in sorted(files):
            if name.startswith("~$"):
                continue  # Word lock files
            if os.path.splitext(name)[1].lower() in SUPPORTED:
                yield os.path.join(root, name)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    cache_dir = sys.argv[1]
    os.makedirs(cache_dir, exist_ok=True)
    for target in sys.argv[2:]:
        if not os.path.exists(target):
            print(f"MISSING  {target}")
            continue
        for path in iter_files(target):
            out = os.path.join(cache_dir, cache_name(path))
            if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(path):
                print(f"cached   {os.path.getsize(out):>8} {out}")
                continue
            ext = os.path.splitext(path)[1].lower()
            try:
                text = CONVERTERS.get(ext, plain_to_text)(path)
            except Exception as e:  # keep going; report the failure
                print(f"FAILED   {path}: {e}")
                continue
            with open(out, "w", encoding="utf-8") as f:
                f.write(f"SOURCE: {os.path.abspath(path)}\n\n{text}")
            print(f"new      {len(text):>8} {out}")


if __name__ == "__main__":
    main()
