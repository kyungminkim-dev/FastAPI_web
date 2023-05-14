from pydantic import BaseModel, EmailStr
from typing import Optional, List
from events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[List]]
    