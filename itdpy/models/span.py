from __future__ import annotations
from typing import Optional
from pydantic import Field
from .base import ITDBaseModel


class Span(ITDBaseModel):
    type: str
    offset: int
    length: int

    tag: Optional[str] = None
