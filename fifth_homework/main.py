# Урок 5. Знакомство с FastAPI
# Задание
# Необходимо создать API для управления списком пользователей. Каждая задача должна
# содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /users — возвращает список всех пользователей.
# — GET /users/{id} — возвращает пользователя с указанным идентификатором.
# — POST /users — добавляет нового пользователя.
# — PUT /users/{id} — обновляет пользователя с указанным идентификатором.
# — DELETE /users/{id} — удаляет пользователя с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.
import logging
from fastapi import FastAPI, HTTPException, Body
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class UserIn(BaseModel):
    name: str
    description: Optional[str] = None


class User(UserIn):
    user_id: int


list_users = [User(user_id=1, name='Pavel'), User(user_id=2, name='Mike')]


@app.get("/users/")
async def show_users():
    logger.info(f'Отработал запрос показать всех пользователей')
    return list_users


@app.get("/users/{user_id}")
async def show_user(user_id: int):
    for user in list_users:
        if user.user_id == user_id:
            logger.info(f'Отработал запрос - показать пользователя id = {user_id}.')
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users/add")
def create_person(attrs: UserIn):
    person = User(user_id=len(list_users)+1, **attrs.dict())
    # добавляем объект в список
    list_users.append(person)
    logger.info(f'Добавлен новый пользователь')
    return person


@app.put("/users/{user_id}")
async def update_user(user_id: int, attrs: UserIn):
    for user in list_users:
        if user.user_id == user_id:
            user.name = attrs.name
            user.description = attrs.description
            logger.info(f'Отработал запрос на изменение пользователя id = {user_id}.')
            return user
    return HTTPException(status_code=404, detail="User not found")


@app.delete("/users/del/{user_id}")
async def delete_user(user_id: int):
    for user in list_users:
        if user.user_id == user_id:
            list_users.remove(user)
            logger.info(f'Отработал DELETE запрос для item id = {user_id}.')
            return list_users
    return {"user_id": user_id}
