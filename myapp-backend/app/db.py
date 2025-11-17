#示例


from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

# 数据库连接

# 1. 修复 URL：添加 sqlite:/// 前缀，并用绝对路径避免混乱
current_dir = os.path.dirname(os.path.abspath(__file__))  # app 目录的绝对路径
print(current_dir)
#print(f"\033[31mcurrent_dir: {current_dir} 用红色显示\033[0m")
db_dir = os.path.join(current_dir, "..")  # db 目录路径（app 的上一级）
db_dir = os.path.normpath(db_dir)
db_path = os.path.join(db_dir, "db\\test.db")  # 数据库文件路径
#print(f"\033[31mdb_path: {db_path} 用红色显示\033[0m")


# 关键：SQLite URL 格式为 sqlite:///文件绝对路径
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.normpath(db_path)}"


#SQLALCHEMY_DATABASE_URL = "../db/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 数据模型
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)



class ChemicalElement(Base):
    """元素周期表数据模型"""
    __tablename__ = "chemical_elements"  # 对应数据库表名

    number = Column(Integer, primary_key=True, comment="原子序数（唯一标识）")
    symbol = Column(String(5), nullable=False, comment="元素符号")
    chineseName = Column(String(20), nullable=False, comment="元素中文名称")
    englishName = Column(String(50), nullable=False, comment="元素英文名称")
    weight = Column(Float, nullable=False, comment="相对原子质量")
    type = Column(String(20), nullable=False, comment="元素类型")
    group = Column(Integer, comment="元素所在族（1-18）")
    period = Column(Integer, nullable=False, comment="元素所在周期（1-7）")
    electronConfig = Column(String(100), nullable=False, comment="电子排布式")

    def __repr__(self):
        """打印模型实例时显示的信息"""
        return f"<ChemicalElement(number={self.number}, symbol='{self.symbol}', chineseName='{self.chineseName}')>"

# 数据库会话依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 简单 CRUD 操作
'''
def create_user(db, user: UserCreate):
    hashed_password = user.password + "_hash"  # 实际项目用加密算法
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
'''




