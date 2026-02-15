# itdpy/formatting/parser.py

from __future__ import annotations

import re
from typing import Dict, List, Tuple


TAG_MAP = {
    "b": "bold",
    "strong": "bold",
    "i": "italic",
    "em": "italic",
    "u": "underline",
    "s": "strike",
    "del": "strike",
    "code": "monospace",
    "spoiler": "spoiler",
}


TAG_PATTERN = re.compile(r"</?(\w+)>")


def parse_html(html: str) -> Dict:

    spans: List[Dict] = []
    stack: List[Tuple[str, int]] = []
    clean_text = ""
    i = 0

    while i < len(html):
        if html[i] == "<":
            match = TAG_PATTERN.match(html[i:])
            if match:
                tag = match.group(1).lower()
                full_tag = match.group(0)

                is_closing = full_tag.startswith("</")

                if tag in TAG_MAP:
                    if not is_closing:
                        stack.append((tag, len(clean_text)))
                    else:
                        for j in range(len(stack) - 1, -1, -1):
                            open_tag, offset = stack[j]
                            if open_tag == tag:
                                stack.pop(j)
                                spans.append({
                                    "type": TAG_MAP[tag],
                                    "offset": offset,
                                    "length": len(clean_text) - offset
                                })
                                break

                i += len(full_tag)
                continue

        clean_text += html[i]
        i += 1

    return {
        "content": clean_text,
        "spans": spans
    }
