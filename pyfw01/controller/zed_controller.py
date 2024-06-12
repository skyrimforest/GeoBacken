
from fastapi import APIRouter
from fastapi.responses import FileResponse
from SkyLogger import get_logger
from service import zed_service
from schema.all_schema import CommandInfo
from starlette.background import BackgroundTasks

router = APIRouter(
    prefix="/zed",
    tags=["zed"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("script")

# 测试组件
@router.post("/")
async def test_users():
    return [{"child_api_status":"ok"}]






