from __future__ import annotations


def get_top_clans(client) -> dict:
    response = client.get("/api/users/stats/top-clans")
    response.raise_for_status()
    return response.json()
