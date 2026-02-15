from __future__ import annotations

from ..models import Me, User, Users
from ._common import build_query


def get_me(client) -> Me:
    response = client.get("/api/users/me")
    response.raise_for_status()
    return Me.model_validate(response.json())


def get_user(client, username: str) -> User:
    response = client.get(f"/api/users/{username}")
    response.raise_for_status()
    return User.model_validate(response.json())


def follow_user(client, username: str) -> bool:
    response = client.post(f"/api/users/{username}/follow")
    response.raise_for_status()
    return True


def unfollow_user(client, username: str) -> bool:
    response = client.delete(f"/api/users/{username}/follow")
    response.raise_for_status()
    return True


def get_followers(client, username: str, page: int = 1, limit: int = 30) -> Users:
    query = build_query({"page": page, "limit": limit})
    response = client.get(f"/api/users/{username}/followers?{query}")
    response.raise_for_status()
    return Users.model_validate(response.json())


def get_following(client, username: str, page: int = 1, limit: int = 30) -> Users:
    query = build_query({"page": page, "limit": limit})
    response = client.get(f"/api/users/{username}/following?{query}")
    response.raise_for_status()
    return Users.model_validate(response.json())
