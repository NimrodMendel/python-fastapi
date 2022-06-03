from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[str]
    title: str
    content: str
    is_published: bool = False
