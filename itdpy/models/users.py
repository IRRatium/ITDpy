from __future__ import annotations

from typing import Any
from pydantic import Field, model_validator

from .base import ITDBaseModel
from .user_lite import UserLite
from .pagination import Pagination


class Users(ITDBaseModel):
    users: list[UserLite] = Field(default_factory=list)
    pagination: Pagination | None = None

    @model_validator(mode="before")
    @classmethod
    def parse_structure(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return {"users": []}

        if "data" in data:
            data = data["data"]

        return {
            "users": data.get("users", []),
            "pagination": data.get("pagination"),
        }

    def __getitem__(self, index):
        return self.users[index]

    def __len__(self):
        return len(self.users)

    def __iter__(self):
        return iter(self.users)

    def __repr__(self):
        return f"<Users count={len(self)}>"
