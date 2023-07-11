from pydantic import BaseModel, validator

from src.settings import settings


class GameOfLifeRequest(BaseModel):
    board: list[list[int]]

    @validator("board")
    def validate_board_size(cls, value: list[list[int]]) -> list[list[int]]:
        if len(value) != settings.BOARD_HEIGHT or len(value[0]) != settings.BOARD_WIDTH:
            raise ValueError(f"Размер поля должен быть равен {settings.BOARD_WIDTH}х{settings.BOARD_HEIGHT}")
        return value


class GameOfLifeResponse(GameOfLifeRequest):
    pass
