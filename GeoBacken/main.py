# fastapi引入
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 基础配置引入
import BaseConfig

# 路由引入
from controller import map_controller,user_controller,drone_controller,disturb_controller


# 创建应用
app = FastAPI()

# 创建路由
app.include_router(map_controller.router)
app.include_router(user_controller.router)
app.include_router(drone_controller.router)
app.include_router(disturb_controller.router)

# 处理cors问题
origins=[
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=BaseConfig.OWN_PORT,reload=True)

