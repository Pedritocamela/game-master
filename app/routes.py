from fastapi import APIRouter, HTTPException
from typing import List
from app.models import GameCreate, GameUpdate, GameResponse
from app import database as db

router = APIRouter(prefix="/api/games", tags=["Games"])

@router.get("/", response_model=List[GameResponse], summary="Obtener todos los juegos")
def get_games():
    """Retorna la lista completa de juegos disponibles."""
    games = db.get_all_games()
    return games

@router.get("/{game_id}", response_model=GameResponse, summary="Obtener un juego por ID")
def get_game(game_id: int):
    """Retorna un juego específico según su ID."""
    game = db.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return game

@router.post("/", response_model=dict, status_code=201, summary="Crear un nuevo juego")
def create_game(game: GameCreate):
    """Crea un nuevo juego en la base de datos."""
    game_id = db.create_game(
        name=game.name,
        platform=game.platform,
        price=game.price,
        discount=game.discount,
        image_url=game.image_url
    )
    if not game_id:
        raise HTTPException(status_code=500, detail="Error al crear el juego")
    return {"id": game_id, "message": "Juego creado exitosamente"}

@router.put("/{game_id}", response_model=dict, summary="Actualizar un juego")
def update_game(game_id: int, game: GameUpdate):
    """Actualiza un juego existente según su ID."""
    existing = db.get_game_by_id(game_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    success = db.update_game(
        game_id=game_id,
        name=game.name,
        platform=game.platform,
        price=game.price,
        discount=game.discount,
        image_url=game.image_url
    )
    if not success:
        raise HTTPException(status_code=500, detail="Error al actualizar el juego")
    return {"message": "Juego actualizado exitosamente"}

@router.delete("/{game_id}", response_model=dict, summary="Eliminar un juego")
def delete_game(game_id: int):
    """Elimina un juego de la base de datos según su ID."""
    existing = db.get_game_by_id(game_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    success = db.delete_game(game_id)
    if not success:
        raise HTTPException(status_code=500, detail="Error al eliminar el juego")
    return {"message": "Juego eliminado exitosamente"}
