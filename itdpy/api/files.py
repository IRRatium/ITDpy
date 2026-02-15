from __future__ import annotations

from ..models import Attachment


def upload_file(client, file_path: str) -> Attachment:
    
    with open(file_path, "rb") as file_obj:
        response = client.post("/api/files/upload", files={"file": file_obj})

    response.raise_for_status()
    return Attachment.model_validate(response.json())
