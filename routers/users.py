from fastapi import APIRouter
from models.user import User


router = APIRouter()

# Временное хранилище для пользователей
user_db = []

@router.post("/register", responses_model=User)
async def register_user(user: User):
    user_db.append(user)
    return user
