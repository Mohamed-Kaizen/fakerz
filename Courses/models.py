import uuid

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Category(models.Model):

    name = fields.CharField(max_length=500, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class PydanticMeta:
        exclude = ["id"]


class Course(models.Model):

    unique_id = fields.UUIDField(unique=True, default=uuid.uuid4)

    title = fields.CharField(max_length=60)

    cover = fields.TextField()

    categories = fields.ManyToManyField("models.Category", related_name="courses")

    is_draft = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class PydanticMeta:
        exclude = ["id"]

Course_Pydantic = pydantic_model_creator(Course, name="Course")
Category_Pydantic = pydantic_model_creator(Category, name="Category")
