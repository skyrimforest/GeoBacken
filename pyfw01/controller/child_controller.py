
from fastapi import APIRouter,BackgroundTasks
from SkyLogger import get_logger
from service import child_service
from schema.all_schema import ChildInfo,PureInfo

router = APIRouter(
    prefix="/child",
    tags=["child"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("child")

# 测试组件
@router.post("/")
async def test_users():
    return [{"child_api_status":"ok"}]

# 注册子节点
@router.post("/register")
async def child_register(ci: ChildInfo):
    try:
        child_service.child_register(ci)
        return {"child_register_status":"ok"}
    except :
        return {"child_register_status":"fail"}

# 触发主节点向子节点发送信息
@router.post("/sendinfo")
async def child_send_info(info:PureInfo,bt:BackgroundTasks):
    try:
        child_service.send_info_child(info,bt)
        return {"child_sendinfo_status":"ok"}
    except:
        return {"child_sendinfo_status":"fail"}

# 父节点接收子节点消息
@router.post("/getinfo")
async def get_child_info(info:PureInfo):
    try:
        child_service.send_info_child(info)
        return {"child_sendinfo_status":"ok"}
    except:
        return {"child_sendinfo_status":"fail"}



