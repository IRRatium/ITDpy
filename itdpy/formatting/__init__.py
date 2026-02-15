from .parser import parse_html
from .validator import validate_spans


def format_html(html: str):
    parsed = parse_html(html)
    validated_spans = validate_spans(parsed["spans"])

    return {
        "content": parsed["content"],
        "spans": validated_spans
    }