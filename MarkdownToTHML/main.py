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

    def close_list():
        nonlocal list_type
        if list_type:
            html_lines.append(f"</{list_type}>")
            list_type = None

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
            else:
                close_list()
                html_lines.append("<pre><code>")
            in_code_block = not in_code_block
            continue

        if in_code_block:
            html_lines.append(html.escape(line))
            continue

        if not stripped:
            close_list()
            continue

        header_match = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if header_match:
            close_list()
            level = len(header_match.group(1))
            html_lines.append(f"<h{level}>{convert_inline(header_match.group(2))}</h{level}>")
            continue

        ul_match = re.match(r"^[-*]\s+(.*)", stripped)
        if ul_match:
            if list_type != "ul":
                close_list()
                html_lines.append("<ul>")
                list_type = "ul"
            html_lines.append(f"<li>{convert_inline(ul_match.group(1))}</li>")
            continue

        ol_match = re.match(r"^\d+\.\s+(.*)", stripped)
        if ol_match:
            if list_type != "ol":
                close_list()
                html_lines.append("<ol>")
                list_type = "ol"
            html_lines.append(f"<li>{convert_inline(ol_match.group(1))}</li>")
            continue

        quote_match = re.match(r"^>\s?(.*)", stripped)
        if quote_match:
            close_list()
            html_lines.append(f"<blockquote>{convert_inline(quote_match.group(1))}</blockquote>")
            continue

        close_list()
        html_lines.append(f"<p>{convert_inline(stripped)}</p>")

    close_list()
    return "\n".join(html_lines)
if __name__ == "__main__":
    main()