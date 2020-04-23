from typing import List

from fakerz.settings import settings
from pydantic import BaseModel, Field


class CourseCreate(BaseModel):

    title: str = Field(..., max_length=60)

    categories: List[str]
