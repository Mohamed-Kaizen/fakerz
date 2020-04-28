import uuid

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):

    name = fields.CharField(max_length=500, unique=True)

    picture = fields.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class PydanticMeta:
        exclude = ["id"]


class Inbox(models.Model):

    slug = fields.UUIDField(unique=True, default=uuid.uuid4)

    title = fields.CharField(max_length=200)

    content = fields.TextField()

    sender = fields.ForeignKeyField("models.User", on_delete=fields.CASCADE)

    users = fields.ManyToManyField("models.User", related_name="Inboxs")

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class PydanticMeta:
        exclude = ["id"]

Inbox_Pydantic = pydantic_model_creator(Inbox, name="Inbox")
User_Pydantic = pydantic_model_creator(User, name="User")
