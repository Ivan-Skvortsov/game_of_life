from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    BOARD_WIDTH: int = 50
    BOARD_HEIGHT: int = 50


settings = Settings()
