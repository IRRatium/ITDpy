from pydantic import Field
from .base import ITDBaseModel

class Pagination(ITDBaseModel):
    page: int = 1
    limit: int = 20
    total: int = 0
    has_more: bool = Field(False, alias="hasMore")
