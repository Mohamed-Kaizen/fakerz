from typing import Any, Dict, List

from fakerz.settings import logger, settings
from fastapi import APIRouter

from . import schema, models

router = APIRouter()


@router.post("/", response_model=models.Course_Pydantic)
async def create_course(user_input: schema.CourseCreate):
    course = models.Course(title=user_input.title)
    await course.save()

    for category in user_input.categories:
        tag, created = await models.Category.get_or_create(name=category.capitalize())
        course.categories.add(tag)

    return await models.Course_Pydantic.from_tortoise_orm(course)


@router.get("/", response_model=List[models.Course_Pydantic])
async def get_all_course():
    return await models.Course_Pydantic.from_queryset(models.Course.all())

@router.get("/category/", response_model=List[models.Category_Pydantic])
async def get_all_category():
    return await models.Category_Pydantic.from_queryset(models.Category.all())
