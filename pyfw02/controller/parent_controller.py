
from fastapi import APIRouter
from fastapi.responses import FileResponse
from SkyLogger import get_logger
from service import parent_service
from schema.all_schema import CommandInfo
from starlette.background import BackgroundTasks

router = APIRouter(
    prefix="/parent",
    tags=["parent"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("parent")

# 测试组件
@router.post("/")
async def test_users():
    return [{"parent_api_status":"ok"}]






