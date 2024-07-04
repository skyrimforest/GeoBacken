
from fastapi import APIRouter
from SkyLogger import get_logger
from service import script_service
from schema.all_schema import CommandInfo
from starlette.background import BackgroundTasks

router = APIRouter(
    prefix="/script",
    tags=["script"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("script")

# 测试组件
@router.post("/")
async def test_users(ci:CommandInfo):
    print(ci.command)
    return [{"username": "Rick"}, {"username": "Morty"}]

# 运行脚本
@router.post("/runscript")
async def run_script(ci:CommandInfo,background_task:BackgroundTasks):
    background_task.add_task(script_service.get_script_process,ci)
    return {
        "success":"执行开始",
    }

# 运行脚本
@router.post("/stopscript")
async def stop_script(ci:CommandInfo,background_task:BackgroundTasks):
    background_task.add_task(script_service.stop_script,ci)
    return {
        "success":"执行开始",
    }

# 查询并获取指令
@router.get("/getscript")
async def get_script():
    script_list=script_service.get_script("config_test")
    return script_list

