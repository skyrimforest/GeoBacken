# 基础引入
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import BaseConfig
# 路由引入
from controller import map_controller

app = FastAPI()

app.include_router(map_controller.router)

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

