from pydantic import BaseModel

# 除下方字段 数据库中也存储id,time等字段
# 仅记录单个子节点的信息,uuid为本次事务
class ChildInfo(BaseModel):
    child_name: str
    child_ip: str
    child_port: str

# 单纯的信息
class PureInfo(BaseModel):
    info: dict
