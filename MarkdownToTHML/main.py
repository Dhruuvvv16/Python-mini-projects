import argparse
import html
import re

CSS = """
body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
       max-width: 760px; margin: 40px auto; padding: 0 20px; line-height: 1.6;
       color: #222; }
h1, h2, h3 { line-height: 1.3; }
code { background: #f2f2f2; padding: 2px 5px; border-radius: 4px;
       font-family: Consolas, Menlo, monospace; }
pre { background: #f2f2f2; padding: 14px; border-radius: 6px; overflow-x: auto; }
pre code { background: none; padding: 0; }
a { color: #0969da; }
blockquote { border-left: 3px solid #ccc; margin: 0; padding-left: 16px; color: #555; }
"""


def convert_inline(text):
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def convert_markdown(markdown_text):
    lines = markdown_text.splitlines()
    html_lines = []
    in_code_block = False
    list_type = None  # "ul" or "ol"
if __name__ == "__main__":
    main()