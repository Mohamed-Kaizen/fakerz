from typing import Dict, List

import httpx
from faker import Faker
from fakerz.settings import logger
from fastapi import APIRouter

router = APIRouter()

fake = Faker()


@logger.catch
async def get_image(*, width: int, height: int) -> httpx.Response:

    client = httpx.AsyncClient()

    return await client.get(f"https://source.unsplash.com/{width}{height}/?face")


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
