from pydantic import BaseModel, Required, Field, EmailStr
from typing import Optional, Any
from datetime import datetime as dt
from .Task import Task


class User(BaseModel):
    user_name: str = Field(Required)
    email: EmailStr = Field(Required)
    tasks: list[Any] | None = Field(None)
    birthdate: dt = Field(Required)
    disabled: bool = Field(Required)

    class Config:
        schema_extra = {
            "example": {
                "user_name": "teste",
                "email": "teste@example.com",
                "tasks": [
                    {
                        "name": "wash the dishes",
                        "status": False,
                        "description": "you need to wash all of your dishes until 6:34 pm"
                    }
                ],
                "birthdate": "2008-09-15",
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
                "disabled": False
            }
        }


class UpdateUser(BaseModel):
    user_name: Optional[str]
    email: Optional[EmailStr]
    tasks: Optional[list[Any]]
    birthdate: Optional[dt]
    disabled: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "user_name": "teste",
                "email": "teste@example.com",
                "tasks": [
                    {
                        "name": "wash the dishes",
                        "status": False,
                        "description": "you need to wash all of your dishes until 6:34 pm"
                    }
                ],
                "birthdate": "2008-09-15",
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
                "disabled": False
            }
        }
