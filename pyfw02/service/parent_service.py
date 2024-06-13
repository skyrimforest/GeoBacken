# 负责与parent板卡通信等功能,系统共有三个子板卡
import requests

from fastapi import BackgroundTasks

# 注册自己
def self_register():
    pass


# 发送心跳信号
def self_heartbeat():
    pass


# 异步发送消息
def send_info_parent(info,bt:BackgroundTasks):
    pass