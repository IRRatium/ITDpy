from typing import Iterable
from ..models import Poll


def vote(
    client,
    post_id: str,
    option_ids: list[str] | str,
) -> Poll:
  
    if isinstance(option_ids, str):
        option_ids = [option_ids]

    if not option_ids:
        raise ValueError("option_ids cannot be empty")

    payload = {
        "optionIds": option_ids
    }

    response = client.post(
        f"/api/posts/{post_id}/poll/vote",
        json=payload
    )
    response.raise_for_status()

    return Poll.model_validate(response.json())
