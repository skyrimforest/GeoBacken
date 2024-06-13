# 引入http网口规范
from fastapi import FastAPI,BackgroundTasks
# 引入服务器
import uvicorn
# 引入命令行参数读取
import argparse
# 引入路由控件
from controller import parent_controller
from controller import zed_controller
# 引入基本配置
import BaseConfig

app = FastAPI()
app.include_router(parent_controller.router)
app.include_router(zed_controller.router)
# 接收环境变量
def parse_args():
    parser = argparse.ArgumentParser(description="Run FastAPI server")
    parser.add_argument(
        "--host", type=str, default="0.0.0.0", help="Host to bind"
    )
    parser.add_argument(
        "--port", type=int, default=10001, help="Port to bind"
    )
    parser.add_argument(
        "--name", type=str, default=BaseConfig.HOST_NAME, help="Child self name"
    )
    parser.add_argument(
        "--venv", type=str, default="pureFast", help="Virtual environment to use"
    )
    parser.add_argument(
        "--phost", type=str, default="0.0.0.0", help="parent node ip"
    )
    parser.add_argument(
        "--pport", type=str, default=10000, help="parent node port"
    )

    return parser.parse_args()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.on_event("startup")
async def startup_event():
    BaseConfig.ARGS=parse_args()

if __name__ == '__main__':
    BaseConfig.ARGS=parse_args()
    uvicorn.run("main:app", host=BaseConfig.ARGS.host, port=BaseConfig.ARGS.port, reload=True)


