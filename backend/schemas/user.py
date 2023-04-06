from pydantic import BaseModel, Field, EmailStr, validator
from typing import Union

class LoginResponse(BaseModel):
    username: str
    email: str
    access_token: str
    token_type: str = "bearer"
    class Config():
        orm_mode = True


class User(BaseModel):
    username:str = Field(
        default=None,
        title="Please enter valid username",
        min_length=5,
    )
    email: EmailStr
    password:str = Field(
        min_length=8
    )

    @validator("username", "email", pre=True)
    def lowercase_strings(cls, value):
        if isinstance(value, str):
            return value.lower()
        return value


class TokenData(BaseModel):
    id: int
    username: Union[str, None] = None
