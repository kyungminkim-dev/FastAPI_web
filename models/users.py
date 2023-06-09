from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[List]]

    class config:
        schema_extra = {
            "example": "fastapi@packt.com",
            "username": "strong!!",
            "events": []
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class config:
        schema_extra = {
            "example": "fastapi@packt.com",
            "password": "string!!",
            "events": [],
        }