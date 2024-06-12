# 负责与child板卡通信等功能,系统共有三个子板卡
import requests

# 子板卡向父节点注册自己,持久化到数据库中
def child_register():
    pass

# 子板卡定时向父报告存活
def child_isalive():
    pass

# 父板卡向子板卡发送信息
def send_info_child():
    pass