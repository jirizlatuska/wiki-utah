#!/usr/bin/env python3
"""Build the expedition atlas PDF from atlas.md + svg/ schematics.

Usage: python3 atlas/build_atlas.py
Output: atlas/za-hranice-casu.pdf (A4, printable)
Requires: python3-markdown, Chromium (path below).
"""
import re, subprocess, sys
from pathlib import Path
import markdown

HERE = Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium"  # adjust if building elsewhere

src = (HERE / "atlas.md").read_text(encoding="utf-8")

# inline the SVG schematics
def inline_svg(m):
    p = HERE / "svg" / f"{m.group(1)}.svg"
    return f'<div class="figure">{p.read_text(encoding="utf-8")}</div>'
src = re.sub(r"\{\{svg:([a-z0-9-]+)\}\}", inline_svg, src)

body = markdown.markdown(src, extensions=["tables", "sane_lists", "md_in_html"])

CSS = """
@page { size: A4; margin: 17mm 16mm; }
body { font-family: "DejaVu Sans", sans-serif; font-size: 10pt; line-height: 1.5; color: #222; }
h1 { page-break-before: always; font-size: 17pt; color: #7a3b1d; border-bottom: 3px solid #b5522a;
     padding-bottom: 5px; margin: 0 0 12px; }
h2 { font-size: 12.5pt; color: #b5522a; margin: 14px 0 6px; }
p { margin: 6px 0; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin: 9px 0; font-size: 9pt; }
th, td { border: 1px solid #b9a; padding: 4px 7px; text-align: left; vertical-align: top; }
th { background: #f3e5dc; }
ul, ol { margin: 6px 0 6px 20px; padding: 0; }
li { margin: 3px 0; }
.figure { margin: 12px 0; page-break-inside: avoid; }
.figure svg { width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; }
.box { border-radius: 6px; padding: 8px 12px; margin: 10px 0; page-break-inside: avoid; font-size: 9.5pt; }
.box p { margin: 3px 0; }
.why   { background: #f0e9df; border-left: 4px solid #8a7a5f; }
.car   { background: #e8eef3; border-left: 4px solid #5a7f9f; }
.aha   { background: #fdf3d8; border-left: 4px solid #d9a521; }
.kid   { background: #e7f2e4; border-left: 4px solid #5f9a52; }
.warn  { background: #fbe9e4; border-left: 4px solid #c0532a; }
.photo { background: #eee9f4; border-left: 4px solid #7d6a9e; }
.note  { background: #eef2ee; border-left: 4px solid #7d8f7d; }
.fire  { background: #fdeade; border-left: 4px solid #e25822; }
.after { display: flex; gap: 10px; margin-top: 14px; page-break-inside: avoid; }
.after .slot { flex: 0 0 150px; height: 100px; border: 2px dashed #bba; border-radius: 6px;
  color: #998; font-size: 9pt; display: flex; align-items: center; justify-content: center; }
.after .lines { flex: 1; height: 100px; border-radius: 6px;
  background: repeating-linear-gradient(#fff, #fff 23px, #cbb 24px); border-bottom: 1px solid #cbb; }
.diarypage { page-break-before: always; }
.diarypage h2 { font-size: 14pt; }
.diarypage .slot.big { height: 300px; border: 2px dashed #bba; border-radius: 8px; color: #998;
  font-size: 24pt; display: flex; align-items: center; justify-content: center; margin: 14px 0; }
.diarypage .lines.tall { height: 480px; background: repeating-linear-gradient(#fff, #fff 27px, #cbb 28px); }
.cover { text-align: center; padding-top: 200px; page-break-after: always; }
.covertop { font-size: 12pt; color: #886; letter-spacing: 2px; text-transform: uppercase; }
.covertitle { font-size: 34pt; color: #7a3b1d; border: none !important; page-break-before: avoid !important;
  margin: 18px 0 6px !important; }
.coversub { font-size: 15pt; color: #444; }
.coverline { font-size: 11pt; color: #997; margin-top: 20px; }
.coverver { font-size: 9.5pt; color: #aa9; margin-top: 60px; }
.preface h1 { page-break-before: avoid; }
.colophon { margin-top: 30px; font-size: 9pt; color: #555; border-top: 1px solid #ccc; padding-top: 8px; }
del { color: #888; }
"""

html = f'<!DOCTYPE html><html lang="cs"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
(HERE / "atlas.html").write_text(html, encoding="utf-8")

pdf = HERE / "za-hranice-casu.pdf"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                str(HERE / "atlas.html")], check=True, capture_output=True)
print(f"OK {pdf}")
