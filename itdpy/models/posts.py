from __future__ import annotations

from typing import Any

from pydantic import Field, model_validator

from .base import ITDBaseModel
from .post import Post


class Posts(ITDBaseModel):
    posts: list[Post] = Field(default_factory=list)
    limit: int | None = None
    next_cursor: str | None = Field(None, alias="nextCursor")
    has_more: bool | None = Field(None, alias="hasMore")

    @model_validator(mode="before")
    @classmethod
    def parse_structure(cls, data: Any) -> Any:
        if isinstance(data, dict) and "data" in data:
            data = data["data"]

        if isinstance(data, list):
            return {"posts": data}

        if isinstance(data, dict):
            posts_list = data.get("posts") or data.get("items") or []
            pagination = data.get("pagination", {})

            return {
                "posts": posts_list,
                "limit": pagination.get("limit"),
                "nextCursor": pagination.get("nextCursor"),
                "hasMore": pagination.get("hasMore"),
            }

        return {"posts": []}

    def __iter__(self):
        return iter(self.posts)

    def __getitem__(self, item):
        return self.posts[item]

    def __len__(self):
        return len(self.posts)

    def __repr__(self) -> str:
        return f"<Posts count={len(self)}>"
