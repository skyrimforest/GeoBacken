from pydantic import BaseModel


class CommandInfo(BaseModel):
    command: str
    arguments: list

# 除下方字段 数据库中也存储id,time等字段
# 仅记录单个子节点的信息,uuid为本次事务
class ChildInfo(BaseModel):
    uuid:str
    child_number: str
    child_name: str
    child_ip_port: str
