from typing import Optional
from pydantic import BaseModel

class MovieSchema(BaseModel):
    id: int | None = None
    title: str
    director: str
    year: int
        