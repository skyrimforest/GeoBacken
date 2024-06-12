
from fastapi import APIRouter
from fastapi.responses import FileResponse
from SkyLogger import get_logger
import BaseConfig


router = APIRouter(
    prefix="/tdoa",
    tags=["tdoa"],
    responses={404: {"description": "Not found"}}
)
