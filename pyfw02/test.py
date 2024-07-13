import asyncio

import requests
import datetime
import aiohttp

if __name__ == '__main__':
    # print(datetime.datetime.now())
    data={
        "info":{
            "hello":"233",
            "test":"haha",
        }
    }
    # http://192.168.227.1:10001/parent/recvinfo
    async def test():
        async with aiohttp.ClientSession() as session:
            async with session.get("http://192.168.227.1:10001/") as res:
                print(await res.text())
    asyncio.run(test())


# import aiohttp
# import asyncio
# from API import parent_api
# import BaseConfig
# from SkyLogger import get_logger
#
# logger = get_logger(__name__)
#
# async def send_info():
#     self_info = {
#         "child_name": BaseConfig.HOST_NAME,
#         "child_ip": BaseConfig.HOST_IP,
#         "child_port": BaseConfig.HOST_PORT
#     }
#     async with aiohttp.ClientSession() as session:
#         while True:
#             try:
#                 async with session.post(parent_api.API['register'], json=self_info) as res:
#                     logger.info(await res.text())
#             except Exception as e:
#                 print(e)
#                 logger.info('主节点未上线或出现问题,请确认...')
#             await asyncio.sleep(5)  # 模拟后台任务，每隔5秒执行一次
#
# if __name__ == '__main__':
#    asyncio.run(send_info())
