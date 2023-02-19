from pydantic import BaseModel, Field, Required
from typing import Optional, Any


class Task(BaseModel):
    name: str = Field(Required)
    status: bool = Field(Required)
    description: str = Field(Required)

    class Config:
        content: Any
        status_code: int
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "wash the dishes",
                "status": False,
                "description": "you need to wash all of your dishes until 6:34 pm"
            }
        }


class UpdateTask(BaseModel):
    name: Optional[str]
    status: Optional[bool]
    description: Optional[str]

    class Config:
        content: Any
        status_code: int
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "wash the dishes",
                "status": False,
                "description": "you need to wash all of your dishes until 6:34 pm"
            }
        }
