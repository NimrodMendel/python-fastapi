from datetime import datetime

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    is_published: bool = False
    created_at: datetime
    updated_at: datetime
