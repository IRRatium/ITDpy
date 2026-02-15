from __future__ import annotations

from typing import List
from pydantic import Field
from .base import ITDBaseModel


class PollOption(ITDBaseModel):
    text: str
    id: str
    position: int
    votesCount: int


class Poll(ITDBaseModel):
    question: str
    options: List[PollOption]
    multiple_choice: bool = Field(False, alias="multipleChoice")

    @classmethod
    def from_simple(
        cls,
        question: str,
        options: list[str],
        multiple_choice: bool = False,
    ) -> "Poll":

        if len(options) < 2:
            raise ValueError("Poll must contain at least 2 options")

        if len(options) > 10:
            raise ValueError("Poll cannot contain more than 10 options")

        return cls(
            question=question,
            options=[PollOption(text=o) for o in options],
            multipleChoice=multiple_choice,
        )
