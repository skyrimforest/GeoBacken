
from fastapi import APIRouter
from fastapi.responses import FileResponse
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
async def test_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

# 运行脚本
@router.post("/runscript")
async def run_script(ci:CommandInfo,background_task:BackgroundTasks):
    background_task.add_task(script_service.run_script,ci)
    return {
        "success":"执行开始",
    }



