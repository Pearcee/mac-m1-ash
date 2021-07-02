from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class TestBase(BaseModel):
    email: str

class TestCreate(UserBase):
    password: str

class Test(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    signup_ts: datetime
    friends: List[int] = []

    class Config:
        orm_mode = True


