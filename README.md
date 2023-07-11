<div id="top"></div>
<div align="center">
<h1>Сервис "Игра Жизнь".</h1>
</div>

## О проекте
Игра «Жизнь» [(англ. Conway's Game of Life)](https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%C2%AB%D0%96%D0%B8%D0%B7%D0%BD%D1%8C%C2%BB) — клеточный автомат, придуманный английским математиком Джоном Конвеем в 1970. <br>
В рамках проекта реализован web-сервис, который задаёт замкнутое поле 50х50 клеток, и, по правилам игры "жизнь", рандомно размещзает на нём "живые клетки". После этого, на каждый запрос сервис обрабатывает текущее изменение состояния поля и отдаёт результат.
<p align="right">(<a href="#top">наверх</a>)</p>

## Использованные технологии
* [FastAPI](https://fastapi.tiangolo.com/)
<p align="right">(<a href="#top">наверх</a>)</p>

## Установка
Склонируйте проект на Ваш компьютер
   ```sh
   git clone https://github.com/Ivan-Skvortsov/game_of_life.git
   ```
Перейдите в папку с проектом
   ```sh
   cd game_of_life
   ```
Создайте виртуальное окружение, активируйте его и установите необходимые зависимости
- Если вы используете пакетный менеджер `pip`
   ```sh
    python3.11 -m venv venv
    . venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt
   ```
 - Если вы используете пакетный менеджер `poetry`:
   ```sh
   poetry config virtualenvs.in-project true
   poetry env use $(which python3.11)
   poetry shell
   poetry install
   ```  
<p align="right">(<a href="#top">наверх</a>)</p>


## Использование
Для запуска проекта выполните команду
```sh
python run.py
```
 - Приложение будет доступно по адресу http://127.0.0.1:8000/
 - Кнопка `Начать новую игру` создаёт новую игру с рандомно расставлеными "живыми" клетками.
 - Кнопка `Сделать шаг` обновляет текущее состояние клеток, согласно правил игры.
<p align="right">(<a href="#top">наверх</a>)</p>

## Об авторе
Автор проекта: Иван Скворцов<br/><br />
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pprofcheg@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Profcheg)
<p align="right">(<a href="#top">наверх</a>)</p>
