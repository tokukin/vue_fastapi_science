from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db, User ,ChemicalElement
from app.schemas import UserCreate, UserOut ,ChemicalElementOut

# 1. 定义核心用户路由（无版本前缀）
user_router = APIRouter(tags=["用户管理"])




@user_router.get("/info", response_model=UserOut)
def get_user_info(
    user_id: int,  # 此时 user_id 是查询参数（URL 中 ?user_id=xxx）
    db: Session = Depends(get_db)
):
    # 查询用户逻辑不变
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


@user_router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).get(user_id)



chemical_router = APIRouter(tags=["化学"])

@chemical_router.get("/element/all", response_model=list[ChemicalElementOut])
def get_chemical_elements(db: Session = Depends(get_db)):
    elements = db.query(ChemicalElement).all()
    if not elements:
        raise HTTPException(status_code=404, detail="元素不存在")
    return elements

@chemical_router.get("/element/info", response_model=ChemicalElementOut)
def get_chemical_element(element_id: int, db: Session = Depends(get_db)):
    element = db.query(ChemicalElement).get(element_id)
    if not element:
        raise HTTPException(status_code=404, detail="元素不存在")
    return element






# 2. 定义版本路由（添加版本前缀）
v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")

# 3. 将用户路由分别挂载到不同版本路由下
v1_router.include_router(user_router, prefix="/users")  # 最终前缀：/api/v1/users
#v2_router.include_router(user_router, prefix="/users")  # 最终前缀：/api/v2/users
v1_router.include_router(chemical_router, prefix="/chemical")  # 最终前缀：/api/v1/chemical
