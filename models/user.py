from pydantic import BaseModel, EmailStr
from datetime import date


class User(BaseModel):
    name: str
    email: EmailStr
    registration_date: date = date.today()
