from __future__ import annotations
from typing import Optional
from .base import ITDBaseModel


class Portal(ITDBaseModel):
    active: bool
    title: str
    url: Optional[str] = None

    def __repr__(self) -> str:
        return f"<Portal title={self.title!r} active={self.active}>"
