
from fastapi import APIRouter
from SkyLogger import get_logger


router = APIRouter(
    prefix="/backen",
    tags=["backen"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("backen")

# 测试组件
@router.post("/")
async def test_users():
    return [{"child_api_status":"ok"}]






