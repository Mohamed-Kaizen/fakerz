import jwt
import pendulum
from fakerz.settings import settings

def create_access_token(*, data: dict, expires_in_minutes: int):

    expire = pendulum.now().add(minutes=expires_in_minutes)

    data.update({"exp": expire})

    encoded_jwt = jwt.encode(
        payload=data, key=settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt
