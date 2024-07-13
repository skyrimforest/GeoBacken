import os
import socket

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

# 日志文件夹
LOG_PATH=ROOT_DIR+'/loginfo'
# 启动参数
ARGS=None
# 本机名称
HOST_NAME=socket.gethostname()
# 自己的IP
HOST_IP=socket.gethostbyname(HOST_NAME)
# 自己的PROT
HOST_PORT=10000
