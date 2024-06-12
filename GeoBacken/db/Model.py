import sqlite3

conn=sqlite3.connect("database.db")
cur=conn.cursor()

# 表中对应的类都在schema文件夹下
# 表1: userinfo

# ------------创建阶段------------

# class UserInfo(BaseModel):
#     username:TEXT           # 用户名
#     password:TEXT           # 密码
#     email:TEXT              # 邮箱
# 另外会自动添加id作为主键,同时记录注册时间
user_info_table_sql="""
create table if not exists imageinfo (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    email TEXT,
    start_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now'))
)
"""

# 无人机信息
# class DroneInfo(BaseModel):
#     dronename:str           # 无人机名称
#     frequency:int           # 频率
#     sample:list             # 频谱样例
#     other:str               # 其他信息
user_info_table_sql="""
create table if not exists imageinfo (
    id INTEGER PRIMARY KEY,
    dronename TEXT,
    frequency FLOAT,
    sample TEXT,
    other TEXT,
    start_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now'))
)
"""

# ------------执行阶段------------
cur.execute(
    user_info_table_sql
)

conn.commit()
conn.close()

