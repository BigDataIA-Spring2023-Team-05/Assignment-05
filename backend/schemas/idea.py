from pydantic import BaseModel, Field, EmailStr, validator
from typing import Union

class MVPIdea(BaseModel):
    idea_title:str = Field(
        title="Please enter valid idea title",
        min_length=5,
    )
    features:str = Field(
        title="Please enter valid fetaure",
        min_length=5,
    )

    class Config:
        orm_mode = True


class EmailRate(BaseModel):
    rating:int = Field(
        title="Please enter valid rating",
    )
    feedback:str = Field(
        title="Please enter valid feedback",
        min_length=5,
    )
