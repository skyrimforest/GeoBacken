# 负责与child板卡通信等功能,系统共有三个子板卡
# 引入http
import requests
# 引入日期
import datetime
# 引入基本配置
import BaseConfig
# 引入子节点信息类型
from schema.all_schema import ChildInfo, PureInfo
# 引入child数据库操作
from mapper import child_mapper
# 引入日志
from SkyLogger import get_logger
# 引入后台任务
from fastapi import BackgroundTasks
from API import child_api

logger = get_logger("child_service")
test_ci = ChildInfo(
    child_name="skyrim-child01",
    child_ip="localhost",
    child_port="10001")

child_dict = {}


# 子板卡向父节点注册自己,以便发送信息
def child_register(ci: ChildInfo):
    global child_dict
    child_name = ci.child_name
    child_ip = ci.child_ip
    child_port = ci.child_port

    uuid = child_name + "@" + child_ip + ":" + child_port
    child_data = {
        "uuid": uuid,
        "child_name": child_name,
        "child_ip": child_ip,
        "child_port": child_port,
        "start_time": datetime.datetime.now()
    }
    if uuid not in child_dict:
        child_dict[uuid] = child_data
        logger.info(f"{uuid} registered")
    else:
        time_before = child_dict[uuid]["start_time"]
        time_after = datetime.datetime.now()
        delta = time_after - time_before
        child_dict[uuid]["start_time"] = time_after
        logger.info(f"{uuid} updated {delta} ago, now it's refreshed.")


# 父板卡向单个子板卡发送信息
def send_info_single(info: PureInfo, ci):
    child_ip = ci['child_ip']
    child_port = ci['child_port']
    child_url = "http://" + child_ip + ":" + child_port + child_api.API['recv']
    data = {
        "info": info.dict()
    }
    print(child_url)
    res = requests.post(child_url, json=data)
    logger.info(f"sent done {res.text}")


# 父板卡向全部个子板卡发送信息
def send_info_child(info: PureInfo, bt: BackgroundTasks):
    global child_dict
    for _, child in child_dict.items():
        bt.add_task(send_info_single, info, child)

    logger.info(f"info sent to all {len(child_dict)} child")
