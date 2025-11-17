from fastapi import FastAPI
from app.routes import v1_router, v2_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="小型项目 API")
app.include_router(v1_router)  
app.include_router(v2_router)  



# 配置允许跨域的源（ origins）
origins = [
    #"http://localhost:5173",  # 你的前端地址（必须精确匹配）
    # 若需要允许所有源（开发环境临时用，生产环境不推荐）：
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源
    allow_credentials=True,  # 允许携带 Cookie
    allow_methods=["*"],  # 允许所有 HTTP 方法（GET、POST、PUT 等）
    allow_headers=["*"],  # 允许所有请求头
)


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}