import random

from src.settings import settings


def create_new_game() -> list[list[int]]:
    """Создает новую игру: 2d-массив, завполненный нулями или единицами в случайном порядке.

    0 - соответствует мертвой клетке, 1 - живой клетке."""
    return [
        [random.randint(0, 1) for _ in range(settings.BOARD_WIDTH)]
        for _ in range(settings.BOARD_HEIGHT)
    ]


def update_game(board: list[list[int]]) -> list[list[int]]:
    """Просматривает все клетки на поле, определяет их статус для нового поколения (в зависимости от соседей)
    и возвращает обновленное игровое поле (2d массив)."""
    updated_board = [[0 for _ in range(settings.BOARD_WIDTH)] for _ in range(settings.BOARD_HEIGHT)]
    for row_idx, row in enumerate(board):
        for column_idx, _ in enumerate(row):
            updated_board[row_idx][column_idx] = 1 if __is_cell_alive(row_idx, column_idx, board) else 0
    return updated_board


def __is_cell_alive(row: int, column: int, board: list[list[int]]) -> bool:
    """Определяет статус клетки для следующего поколения (умрёт или родится).

    Для этого суммирует значения клетки и её соседей в области. Далее, в зависимости от результата:
        - если сумма равна 3 - клетка остаётся живой (или оживает)
        - если сумма равна 4 - клетка остаётся живой только в том случае, если она уже была жива
        - в других случаях клетка умирвает (или остаётся мертвой).

    Отрицательные индексы используются для реализации замкнутого поля."""
    cells = [
        board[row - x][column - y] for x in [1, 0, settings.BOARD_WIDTH - 1] for y in [1, 0, settings.BOARD_HEIGHT - 1]
    ]
    sum_cells = sum(cells)
    return sum_cells == 3 or (sum_cells == 4 and board[row][column] == 1)
