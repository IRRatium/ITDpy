from __future__ import annotations
from typing import Dict, List


def _overlaps(a: Dict, b: Dict) -> bool:
    a_start = a["offset"]
    a_end = a_start + a["length"]

    b_start = b["offset"]
    b_end = b_start + b["length"]

    return not (a_end <= b_start or b_end <= a_start)


def _remove_duplicates(spans: List[Dict]) -> List[Dict]:
    seen = set()
    result = []

    for span in spans:
        key = (span["type"], span["offset"], span["length"])
        if key not in seen:
            seen.add(key)
            result.append(span)

    return result


def _validate_code_rules(spans: List[Dict]) -> List[Dict]:

    monospace_spans = [s for s in spans if s["type"] == "monospace"]
    cleaned = []

    for span in spans:
        if span["type"] == "monospace":
            cleaned.append(span)
            continue

        inside_code = any(
            _overlaps(span, code_span)
            for code_span in monospace_spans
        )

        if inside_code and span["type"] in ("bold", "italic"):
            continue

        cleaned.append(span)

    return cleaned


def _remove_double_underlines(spans: List[Dict]) -> List[Dict]:

    result = []
    for span in spans:
        if span["type"] == "underline":
            duplicate = any(
                s["type"] == "underline"
                and s["offset"] == span["offset"]
                and s["length"] == span["length"]
                for s in result
            )
            if duplicate:
                continue

        result.append(span)

    return result


def validate_spans(spans: List[Dict]) -> List[Dict]:
    spans = sorted(spans, key=lambda s: (s["offset"], s["length"]))

    spans = _remove_duplicates(spans)
    spans = _validate_code_rules(spans)
    spans = _remove_double_underlines(spans)

    return spans
