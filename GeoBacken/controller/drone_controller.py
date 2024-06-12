
from fastapi import APIRouter
from fastapi.responses import FileResponse
from SkyLogger import get_logger

router = APIRouter(
    prefix="/drone",
    tags=["drone"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("drone")

# 测试组件
@router.post("/")
async def test_users():
    return [{"username": "Rick"}, {"username": "Morty"}]




