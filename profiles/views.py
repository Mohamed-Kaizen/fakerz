from typing import Any, Dict, List

import httpx
from faker import Faker
from fakerz.settings import logger, settings
from fastapi import APIRouter

from . import schema, utils

router = APIRouter()

fake = Faker()


@logger.catch
async def get_image(*, width: int, height: int) -> httpx.Response:

    client = httpx.AsyncClient()

    return await client.get(f"https://source.unsplash.com/{width}x{height}/?face")


@router.get("/")
@logger.catch
async def get_profile(
    profile: int = 5, image_width: int = 800, image_height: int = 800
) -> List[Dict]:

    users = []
    try:
        for _ in range(profile):

            response = await get_image(width=image_width, height=image_height)

            logger.info(f"image status {response.status_code}")

            bio = fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)

            user_info: Dict = fake.profile()

            user_info.update(
                {
                    "bio": bio,
                    "image": f"https://images.unsplash.com{response.url.full_path}",
                }
            )

            users.append(user_info)

        return users

    except AttributeError as error:
        logger.opt(exception=True).exception(error)


@router.post("/login/")
async def login(user_input: schema.UserLogin) -> Dict[str, Any]:

    access_token = utils.create_access_token(
        data={"sub": user_input.email, "username": fake.name()},
        expires_in_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    client = httpx.AsyncClient()

    response = await client.get(f"https://source.unsplash.com/800x400/?profile")

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {"username": fake.name(), "picture": f"https://images.unsplash.com{response.url.full_path}"}
    }
