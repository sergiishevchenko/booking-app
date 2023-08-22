from typing import List

from pydantic import BaseModel


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int

    class Config:
        # orm_mode changed name in version 2 of Pydantic
        from_attributes = True


class SHotelInfo(SHotel):
    rooms_left: int

    class Config:
        # orm_mode changed name in version 2 of Pydantic
        from_attributes = True