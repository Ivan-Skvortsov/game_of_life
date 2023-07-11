from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.services import create_new_game, update_game
from src.schemas import GameOfLifeRequest, GameOfLifeResponse


app = FastAPI()


@app.get(
    "/game",
    response_model=GameOfLifeResponse,
    summary="Создать новую игру",
    response_description="Новое игровое поле с рандомно размещенными клетками."
)
def create_game():
    """Создаёт новую игру с рандомно размещенными клетками."""
    return GameOfLifeResponse(board=create_new_game())


@app.post(
    "/game",
    response_model=GameOfLifeResponse,
    summary="Обновить игру (сделать 1 шаг)",
    response_description="Обновленное игровое поле."
)
def update_current_game(current_game: GameOfLifeRequest):
    """Проверяет состояние клеток на поле и возвращает обновленную игру."""
    return GameOfLifeResponse(board=update_game(current_game.board))


app.mount("/", StaticFiles(directory="src/staticfiles", html=True))
