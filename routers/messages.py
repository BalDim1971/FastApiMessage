from fastapi import APIRouter, HTTPException
from models.message import Message
from typing import List

router = APIRouter()

# Временное хранилище для сообщений
messages_db = []


@router.post("/send/", response_model=Message)
async def send_message(message: Message):
    """
    Отправляет сообщение в базу данных
    """
    messages_db.append(message)
    return message


@router.get("/messages/{email}", response_model=List[Message])
async def get_messages(email: str):
    """
    Возвращает все сообщения для указанного email
    """
    user_messages = [mess for mess in messages_db if mess.email == email]
    if not user_messages:
        raise HTTPException(status_code=404, detail="Сообщений не найдено")
    return user_messages
