from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определяем модель данных для пользователя
class User(BaseModel):
    id: int
    name: str
    email: str

# Список пользователей (будем использовать его как временное хранилище)
users = []

# Определяем маршрут для получения всех пользователей
@app.get('/users', response_model=List[User])
def get_users():
    return users

# Определяем маршрут для добавления нового пользователя
@app.post('/users', response_model=User)
def create_user(user: User):
    users.append(user)
    return user

# Запускаем приложение с помощью Uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

    # uvicorn main: app --reload - запуск приложения