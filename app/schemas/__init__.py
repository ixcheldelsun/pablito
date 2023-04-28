from typing import Optional

from pydantic import BaseModel, EmailStr, Field


def Weeding(BaseModel):
    data = dict = Field(..., example={"name": "Weeding", "price": 1000})
    class Config:
        schema_extra = {
            "example": {
                "What is the name of the main event": "Ceremony",
                "Who is the host of the main event?": "Daniel",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}