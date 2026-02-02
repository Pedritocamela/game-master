from pydantic import BaseModel, Field
from typing import Optional

class GameBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del juego")
    platform: str = Field(..., min_length=1, max_length=50, description="Plataforma (PC, PlayStation, Xbox, Nintendo)")
    price: float = Field(..., gt=0, le=999.99, description="Precio del juego en euros")
    discount: int = Field(default=0, ge=0, le=100, description="Porcentaje de descuento")
    image_url: str = Field(..., min_length=1, max_length=500, description="URL de la imagen del juego")

class GameCreate(GameBase):
    pass

class GameUpdate(GameBase):
    pass

class GameResponse(GameBase):
    id: int = Field(..., description="ID único del juego")

    class Config:
        from_attributes = True
