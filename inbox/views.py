from typing import Any, Dict, List

import httpx
from fakerz.settings import logger, settings
from fastapi import APIRouter

from . import models, schema

router = APIRouter()


@router.post("/", response_model=models.Inbox_Pydantic)
async def create_inbox(user_input: schema.InboxCreate):
    client = httpx.AsyncClient()

    response = await client.get("https://source.unsplash.com/400x400/?profile")

    sender, created = await models.User.get_or_create(
        name=user_input.sender.capitalize()
    )

    sender.picture = f"https://images.unsplash.com{response.url.full_path}"

    await sender.save()

    inbox = models.Inbox(
        title=user_input.title, content=user_input.content, sender=sender
    )

    await inbox.save()

    for username in user_input.users:

        user, created = await models.User.get_or_create(name=username.capitalize())

        user.picture = f"https://images.unsplash.com{response.url.full_path}"

        await user.save()

        await inbox.users.add(user)

    return await models.Inbox_Pydantic.from_tortoise_orm(inbox)


@router.get("/")
async def get_all_inbox():
    inbox_list = []
    inboxes = await models.Inbox.all()
    for inbox in inboxes:
        sender = await inbox.sender
        inbox_list.append(
            {
                "slug": inbox.slug,
                "title": inbox.title,
                "content": inbox.content,
                "sender": await models.User_Pydantic.from_tortoise_orm(sender),
                "users": await models.User_Pydantic.from_queryset(inbox.users.all()),
                "created_at": inbox.created_at,
            }
        )
    return inbox_list


@router.get("/users/", response_model=List[models.User_Pydantic])
async def get_all_user():
    return await models.User_Pydantic.from_queryset(models.User.all())
