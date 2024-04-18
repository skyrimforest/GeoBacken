from pydantic import BaseModel

# 用户信息
class UserInfo(BaseModel):
    username:str           # 用户名
    password:str           # 密码
    email:str              # 邮箱

# 无人机信息
class DroneInfo(BaseModel):
    dronename:str           # 无人机名称
    frequency:int           # 频率
    sample:str              # 频谱样例,实际上是list转成的str
    other:str               # 其他信息
