from __future__ import annotations

from typing import Optional
from pydantic import Field

from .base import ITDBaseModel
from .span import Span


class PostUpdate(ITDBaseModel):
    id: str
    content: Optional[str] = None
    spans: list[Span] = Field(default_factory=list)

    updated_at: str = Field(..., alias="updatedAt")

    def __repr__(self) -> str:
        return f"<PostUpdate {self.id}>"
