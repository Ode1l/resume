"""Render the compact HTML CV with original typography and clickable links."""
from pathlib import Path
import subprocess
import json

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "compact-fintech-resume.html"
OUT = ROOT / "output/pdf/Jiaheng Li Full Stack Software Engineer Resume 2026-10-09.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
RUNTIME = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies"
NODE = RUNTIME / "node/bin/node"
PLAYWRIGHT = RUNTIME / "node/node_modules/playwright/index.mjs"

OUT.parent.mkdir(parents=True, exist_ok=True)
# Playwright launches its own temporary profile, never the signed-in session.
render = f"""
import {{ chromium }} from {json.dumps(PLAYWRIGHT.as_uri())};
const browser = await chromium.launch({{
    executablePath: {json.dumps(CHROME)}, headless: true
}});
try {{
    const page = await browser.newPage();
    await page.goto({json.dumps(SOURCE.as_uri())}, {{waitUntil: 'load'}});
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({{
        path: {json.dumps(str(OUT))}, format: 'A4',
        printBackground: true, preferCSSPageSize: true
    }});
}} finally {{
    await browser.close();
}}
"""
subprocess.run([str(NODE), "--input-type=module", "-e", render],
               check=True, capture_output=True, timeout=60)

reader = PdfReader(OUT)
assert len(reader.pages) == 1, f"Expected one page, got {len(reader.pages)}"
text = reader.pages[0].extract_text()
assert "Full Stack Software Engineer" in text
assert "Python" in text and "Go" in text
print(OUT)
print("Pages:", len(reader.pages), "Link annotations:", len(reader.pages[0].get("/Annots", [])))
