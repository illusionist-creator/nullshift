"""Wraps src/page.html into the standalone index.html that GitHub Pages serves."""
from pathlib import Path

root = Path(__file__).parent
page = (root / "src" / "page.html").read_text(encoding="utf-8")
head, body = page.split("</style>\n", 1)
html = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head + "</style>\n</head>\n<body>\n" + body.rstrip("\n") + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(html, encoding="utf-8", newline="\n")
print("index.html", len(html), "bytes")
