from __future__ import annotations

from typing import Any
from pydantic import Field, model_validator

from .base import ITDBaseModel
from .comment import Comment
from .pagination import Pagination


class CommentsData(ITDBaseModel):
    comments: list[Comment] = Field(default_factory=list)
    pagination: Pagination | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_structure(cls, payload: Any) -> Any:
        if not isinstance(payload, dict):
            return {"comments": []}

        # если это replies
        if "replies" in payload:
            return {
                "comments": payload.get("replies", []),
                "pagination": payload.get("pagination"),
            }

        # если обычный список комментариев
        if "comments" in payload:
            return payload

        return {"comments": []}


class Comments(ITDBaseModel):
    data: CommentsData

    @model_validator(mode="before")
    @classmethod
    def parse_structure(cls, payload: Any) -> Any:
        if isinstance(payload, dict) and "data" in payload:
            return payload

        if isinstance(payload, dict):
            return {"data": payload}

        return {"data": {"comments": []}}

    def __iter__(self):
        return iter(self.data.comments)

    def __getitem__(self, item):
        return self.data.comments[item]

    def __len__(self):
        return len(self.data.comments)

    def __repr__(self) -> str:
        return f"<Comments count={len(self)}>"
