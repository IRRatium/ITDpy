from typing import Optional
from pydantic import Field
from .base import ITDBaseModel

class Attachment(ITDBaseModel):
    id: str
    type_: Optional[str] = Field(None, alias="type")
    url: str
    thumbnail_url: Optional[str] = Field(None, alias="thumbnailUrl")
    filename: Optional[str] = None
    mime_type: Optional[str] = Field(None, alias="mimeType")
    size: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    order: Optional[int] = None

