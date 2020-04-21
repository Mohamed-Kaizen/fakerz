from fakerz.settings import settings
from pydantic import BaseModel, EmailStr, Field, validator
from . import validators

class UserLogin(BaseModel):

    password: str = Field(
        ...,
        min_length=settings.MINIMUM_PASSWORD_LENGTH,
        max_length=settings.MAXIMUM_PASSWORD_LENGTH,
    )

    email: EmailStr

    @validator("email")
    def extra_validation_on_email(cls, value: str):

        local_part, domain = value.split("@")

        validators.validate_reserved_name(value=local_part, exception_class=ValueError)

        validators.validate_confusables_email(
            domain=domain, local_part=local_part, exception_class=ValueError
        )

        return value
