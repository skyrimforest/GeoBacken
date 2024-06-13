
from fastapi import APIRouter
from SkyLogger import get_logger
from schema.all_schema import ChildInfo,PureInfo
import BaseConfig

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

@router.post("/recvinfo")
async def recv_info(someinfo:PureInfo):
    print(someinfo)
    print(BaseConfig.ARGS)
    return {"parent_recvinfo_status":"ok"}





