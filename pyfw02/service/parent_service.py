# 负责与parent板卡通信等功能,系统共有三个子板卡
import socket
from fastapi import BackgroundTasks
from schema.all_schema import ChildInfo
import BaseConfig
import asyncio
import aiohttp
from API import parent_api
from SkyLogger import get_logger
logger = get_logger("parent_service")

# 每隔10秒注册自己
async def self_register(sleep_time=10):
    self_info={
        "child_name":BaseConfig.HOST_NAME,
        "child_ip":BaseConfig.HOST_IP,
        "child_port":BaseConfig.HOST_PORT
    }
    await send_info_parent(self_info,sleep_time)

# 异步发送消息
async def send_info_parent(info,sleep_time):
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.post(parent_api.API['register'], json=info) as res:
                    logger.info(await res.text())
            except Exception as e:
                print(e)
                logger.info('主节点未上线或出现问题,请确认...')
            await asyncio.sleep(sleep_time)  # 模拟后台任务，每隔5秒执行一次


if __name__ == '__main__':
    self_register()