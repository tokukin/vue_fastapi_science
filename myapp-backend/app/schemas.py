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


'''

   
    number = Column(Integer, primary_key=True, comment="原子序数（唯一标识）")
     symbol = Column(String(5), nullable=False, comment="元素符号")
      chineseName = Column(String(20), nullable=False, comment="元素中文名称")
     englishName = Column(String(50), nullable=False, comment="元素英文名称")
      weight = Column(Float, nullable=False, comment="相对原子质量")
      type = Column(String(20), nullable=False, comment="元素类型")
      group = Column(Integer, comment="元素所在族（1-18）")
      period = Column(Integer, nullable=False, comment="元素所在周期（1-7）")
      electronConfig = Column(String(100), nullable=False, comment="电子排布式")
'''