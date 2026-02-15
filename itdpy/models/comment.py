from __future__ import annotations

from pydantic import AliasChoices, Field

from .attachment import Attachment
from .base import ITDBaseModel
from .user_lite import UserLite


class Comment(ITDBaseModel):
    id: str
    content: str | None = None

    likes_count: int = Field(0, alias="likesCount", validation_alias=AliasChoices("likesCount", "likkesCount"))
    replies_count: int = Field(0, alias="repliesCount")
    is_liked: bool = Field(False, alias="isLiked")

    created_at: str = Field(..., alias="createdAt")

    author: UserLite | None = None
    attachments: list[Attachment] = Field(default_factory=list)
    replies: list[Comment] = Field(default_factory=list)
