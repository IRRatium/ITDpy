from __future__ import annotations

from ..models import Comment, Comments
from ._common import build_query, normalize_id_list, truthy_response_status
from ..formatting import format_html

def create_comment(
    client,
    post_id: str,
    content: str,
    attachment_ids: list[str] | str | None = None,
) -> Comment:
    
    payload = {
            "content": content,
            "attachmentIds": normalize_id_list(attachment_ids),
    }
    
    response = client.post(f"/api/posts/{post_id}/comments", json=payload)
    response.raise_for_status()
    return Comment.model_validate(response.json())


def reply_to_comment(
    client,
    comment_id: str,
    content: str,
    attachment_ids: list[str] | str | None = None,
) -> Comment:
    payload = {
        "content": content,
        "attachmentIds": normalize_id_list(attachment_ids),
    }
    response = client.post(f"/api/comments/{comment_id}/replies", json=payload)
    response.raise_for_status()
    return Comment.model_validate(response.json())


def delete_comment(client, comment_id: str) -> bool:
    response = client.delete(f"/api/comments/{comment_id}")
    if response.status_code == 204:
        return True
    response.raise_for_status()
    return False


def like_comment(client, comment_id: str) -> bool:
    response = client.post(f"/api/comments/{comment_id}/like")
    response.raise_for_status()
    return truthy_response_status(response.status_code)


def unlike_comment(client, comment_id: str) -> bool:
    response = client.delete(f"/api/comments/{comment_id}/like")
    response.raise_for_status()
    return truthy_response_status(response.status_code)


def get_comments(client, post_id: str, limit: int = 20, sort: str = "popular") -> Comments:
    allowed_sorts = {"popular", "newest", "oldest"}

    if sort not in allowed_sorts:
        raise ValueError(
            f"Invalid sort value '{sort}'. "
            f"Allowed values: {', '.join(allowed_sorts)}"
        )
    
    query = build_query({"limit": limit, "sort": sort})
    response = client.get(f"/api/posts/{post_id}/comments?{query}")
    response.raise_for_status()
    return Comments.model_validate(response.json())

def get_replies(client, comment_id: str, sort: str = "newest") -> Comments:
    allowed_sorts = {"popular", "newest", "oldest"}

    if sort not in allowed_sorts:
        raise ValueError(
            f"Invalid sort value '{sort}'. "
            f"Allowed values: {', '.join(allowed_sorts)}"
        )
    query = build_query({"sort": sort})
    response = client.get(f"/api/comments/{comment_id}/replies?{query}")
    response.raise_for_status()
    return Comments.model_validate(response.json())
