from __future__ import annotations

from typing import Any, Optional

from pydantic import AliasChoices, Field, model_validator

from .attachment import Attachment
from .base import ITDBaseModel
from .comment import Comment
from .user_lite import UserLite
from .span import Span
from .poll import Poll


class Post(ITDBaseModel):
    @model_validator(mode="before")
    @classmethod
    def unwrap_data(cls, data: Any) -> Any:
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict):
            return data["data"]
        return data

    id: str
    content: Optional[str] = None
    spans: list[Span] = Field(default_factory=list)

    likes_count: int = Field(
        0,
        alias="likesCount",
        validation_alias=AliasChoices("likesCount", "likkesCount"),
    )
    comments_count: int = Field(0, alias="commentsCount")
    reposts_count: int = Field(0, alias="repostsCount")
    views_count: int = Field(0, alias="viewsCount")

    is_liked: bool = Field(False, alias="isLiked")
    is_reposted: bool = Field(False, alias="isReposted")
    is_viewed: bool = Field(False, alias="isViewed")
    is_owner: bool = Field(False, alias="isOwner")
    is_pinned: bool = Field(False, alias="isPinned")

    created_at: str = Field(..., alias="createdAt")

    author: Optional[UserLite] = None
    attachments: list[Attachment] = Field(default_factory=list)

    wall_recipient_id: Optional[str] = Field(None, alias="wallRecipientId")
    wall_recipient: Optional[UserLite] = Field(None, alias="wallRecipient")

    original_post: Optional["Post"] = Field(None, alias="originalPost")

    poll: Optional[Poll] = None

    def __repr__(self) -> str:
        return f"<Post {self.id}>"

Post.model_rebuild()
