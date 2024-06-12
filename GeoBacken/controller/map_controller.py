
from fastapi import APIRouter
from fastapi.responses import FileResponse
from SkyLogger import get_logger
import BaseConfig


router = APIRouter(
    prefix="/map",
    tags=["map"],
    responses={404: {"description": "Not found"}}
)

logger = get_logger("map")

# 测试组件
@router.post("/")
async def test_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

# 返回北京地图
@router.get("/images/beijing/{z}/{x}/{y}")
async def get_image_beijing(z: str, x: str, y: str):
    try:
        path=BaseConfig.MAP_PATH+f"/GaoDeBeiJing/{z}/{x}/{y}"
        response=FileResponse(path, media_type="image/jpeg")
    except:
        return {
            "message": "No pic"
        }
    return response

# 返回上海地图
@router.get("/images/shanghai/{z}/{x}/{y}")
async def get_image_shanghai(z: str, x: str, y: str):
    try:
        path=BaseConfig.MAP_PATH+f"/GaoDeShangHai/{z}/{x}/{y}"
        response=FileResponse(path, media_type="image/jpeg")
    except:
        return {
            "message": "No pic"
        }
    return response

# 返回广州地图
@router.get("/images/guangzhou/{z}/{x}/{y}")
async def get_image_guangzhou(z: str, x: str, y: str):
    try:
        path=BaseConfig.MAP_PATH+f"/GaoDeGuangZhou/{z}/{x}/{y}"
        response = FileResponse(path, media_type="image/jpeg")
    except:
        return {
            "message": "No pic"
        }
    return response

# 返回深圳地图
@router.get("/images/shenzhen/{z}/{x}/{y}")
async def get_image_shenzhen(z: str, x: str, y: str):
    try:
        path=BaseConfig.MAP_PATH+f"/GaoDeShenZhen/{z}/{x}/{y}"
        response = FileResponse(path, media_type="image/jpeg")
    except:
        return {
            "message": "No pic"
        }
    return response

# 返回完整的中国地图
@router.get("/images/whole/{z}/{x}/{y}")
async def get_image_whole(z: str, x: str, y: str):
    try:
        path=BaseConfig.MAP_PATH+f"/GaoDeShenZhen/{z}/{x}/{y}"
        response = FileResponse(path, media_type="image/jpeg")
    except:
        return {
            "message": "No pic"
        }
    return response



