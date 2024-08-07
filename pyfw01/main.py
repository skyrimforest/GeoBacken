# 引入http网口规范
from fastapi import FastAPI
# 引入服务器
import uvicorn
# 引入命令行参数读取
import argparse
# 引入路由控件
from controller import child_controller
from controller import zed_controller
# 引入基本配置
import BaseConfig

app = FastAPI()
app.include_router(child_controller.router)
app.include_router(zed_controller.router)
# 接收环境变量
def parse_args():
    parser = argparse.ArgumentParser(description="Run FastAPI server")
    parser.add_argument(
        "--host", type=str, default=BaseConfig.HOST_IP, help="Host to bind"
    )
    parser.add_argument(
        "--port", type=int, default=BaseConfig.HOST_PORT, help="Port to bind"
    )
    parser.add_argument(
        "--venv", type=str, default="pureFast", help="Virtual environment to use"
    )
    return parser.parse_args()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# 功能状态机:
#   系统启动
#   ->注册阶段,注册一个之后即可开始进行服务,之后也可不断注册子节点
#   ->服务阶段,完成正常的服务需求
#   ->停止阶段,系统正常关闭,持久化记录本次事务

@app.on_event("startup")
async def startup_event():
    pass

if __name__ == '__main__':
    uvicorn.run("main:app", host=BaseConfig.HOST_IP, port=BaseConfig.HOST_PORT)


