# 负责与zed的通信等功能
from utils import tcp_ope
from fastapi import BackgroundTasks
from .parent_service import send_info_parent

# 异步发送消息
def send_info_zed(info,bt:BackgroundTasks):
    pass

# 定时接收消息
def get_info_zed(bt:BackgroundTasks):
    pass

