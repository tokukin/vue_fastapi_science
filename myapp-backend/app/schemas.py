#示例

from pydantic import BaseModel, EmailStr

from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str



class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True  # 支持 ORM 模型直接转换
        from_attributes = True

class ChemicalElementOut(BaseModel):
    number: int
    symbol: str
    chineseName: str
    englishName: str
    weight:float
    type:str
    group:int
    period:int
    electronConfig:str
    class Config:
        orm_mode = True  # 支持 ORM 模型直接转换
        from_attributes = True


