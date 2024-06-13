# 负责与child板卡通信等功能,系统共有三个子板卡
# 引入http
import requests

import BaseConfig
# 引入子节点信息类型
from schema.all_schema import ChildInfo, PureInfo
# 引入child数据库操作
from mapper import child_mapper
# 引入日志
from SkyLogger import get_logger
# 引入后台任务
from fastapi import BackgroundTasks

logger = get_logger("child_service")
test_ci = ChildInfo(
    uuid=BaseConfig.UUID,
    child_name="skyrim-child01",
    child_ip="localhost",
    child_port="10001")

child_list = [
    test_ci
]


# 子板卡向父节点注册自己,持久化到数据库中
def child_register(ci: ChildInfo):
    global child_list
    child_name = ci.child_name
    child_ip = ci.child_ip
    child_port = ci.child_port

    child_data = {
        "ci": ci,
        "heartbeat": 0  # 最大不超过300秒
    }

    child_list.append(child_data)
    child_mapper.child_insert()
    logger.info(f"{child_name}@{child_ip}:{child_port} registered")


# 判断子板卡是否都存活
def child_isalive():
    global child_list
    for idx in range(0, len(child_list)):
        if child_list[idx]["heartbeat"] >= 300:
            child_list.pop(idx)


# 将子板卡心跳间隔重置
def child_update(ci: ChildInfo):
    global child_list

    for idx in range(0, len(child_list)):
        if child_list[idx]["ci"] >= 300:
            child_list.pop(idx)


# 父板卡向子板卡发送信息
def send_info_child(info: PureInfo, bt: BackgroundTasks):
    global child_list
    for child in child_list:
        bt.add_task(send_info_single, info, child)

    logger.info(f"info sent to all {len(child_list)} child")


def send_info_single(info: PureInfo, ci: ChildInfo):
    global child_list
    child_ip = ci.child_ip
    child_port = ci.child_port
    child_url = "http://" + child_ip + ":" + child_port + "/parent/recvinfo"
    data={
        "info":info.dict()
    }
    res = requests.post(child_url, json=data)
    logger.info(f"sent done {res.text}")
