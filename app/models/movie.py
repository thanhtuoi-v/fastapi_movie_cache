from pydantic import BaseModel, Field
from typing import List


class MovieBase(BaseModel):
    title: str
    year: int
    genres: List[str]
    duration: int
    description: str
    director: str

class Movie(MovieBase):
    id: str = Field(..., alias="_id")

    class Config:
        validate_by_name = True
        from_attributes = True

class MovieCreate(MovieBase):
    pass