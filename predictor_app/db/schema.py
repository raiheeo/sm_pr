from  pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserProfileSchema(BaseModel):

    id: int
    first_name: str
    last_name: Optional[str]
    username: str
    email: EmailStr
    password: str
    age: Optional[int]
    phone_number: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class MobileSchema(BaseModel):
    Rating: int
    Num_Ratings: int
    RAM: int
    ROM: int
    Battery: int
    Processor: str
    Front_Cam: Optional[int] = None
    Price_INR: Optional[int] = None

    class Config:
        from_attributes = True