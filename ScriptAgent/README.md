
这个项目用于管理ubuntu下脚本运行的
主体使用fastapi开发,可以使用脚本指定ip与端口
因为使用了subprocess库,因此windows下是不能使用该项目的
默认ip为本机ip,端口为10000
使用方法:
# 指定端口号为9000运行
python main.py --port 9000
