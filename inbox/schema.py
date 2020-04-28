from typing import List

from fakerz.settings import settings
from pydantic import BaseModel, Field


class InboxCreate(BaseModel):

    title: str = Field(..., max_length=20)

    sender: str

    content: str

    users: List[str]
