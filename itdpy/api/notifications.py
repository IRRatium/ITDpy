from __future__ import annotations

from ..models.notifications import Notifications
from ._common import build_query, normalize_id_list


def get_notifications(client, offset: int = 0, limit: int = 20) -> Notifications:
    query = build_query({"offset": offset, "limit": limit})
    response = client.get(f"/api/notifications/?{query}")
    response.raise_for_status()
    return Notifications.model_validate(response.json())


def mark_notification_read(client, notification_id: str) -> bool:
    response = client.post(f"/api/notifications/{notification_id}/read")
    response.raise_for_status()
    data = response.json()
    return bool(data.get("success", False))


def mark_all_notification_read(client, notification_ids: list[str] | str | None) -> int:
    normalized = normalize_id_list(notification_ids)
    if not normalized:
        return 0

    response = client.post("/api/notifications/read-batch", json=normalized)
    response.raise_for_status()
    data = response.json()
    return int(data.get("count", 0))
