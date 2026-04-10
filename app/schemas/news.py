from pydantic import BaseModel
from typing import Optional

class WeatherUpdate(BaseModel):
    title: str
    description: str
    date: str
    imageUrl: Optional[str] = ""

class WeatherUpdateResponse(WeatherUpdate):
    id: str
