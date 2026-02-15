from typing import Optional
from .base import ITDBaseModel

class Pin(ITDBaseModel):
    slug: str
    name: str
    description: Optional[str] = None
    pin: Optional["Pin"] = None
    
