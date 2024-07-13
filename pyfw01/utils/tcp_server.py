# 该文件用于与板卡建立tcp连接并传输数据
# 该文件作为一个简单的服务器端
import socket


# 具体思路为对传输的数据进行关键字分割,之后就可以获取每条信息

# 获取socket
def get_server_socket():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost',8001))
        server_socket.listen(5)
        return server_socket
    except:
        return None


# 和服务器连接
def listen_to_client(server_socket):
    print("开始运行")
    while True:
        try:
            conn,addr=server_socket.accept()
            data_bytes=conn.recv(2048)
            print(data_bytes.decode())
            conn.sendall("hello@skyrim@07131303".encode())
            print("send done")
            conn.close()
            return {"success": True}
        except Exception as e:
            print(e)
            return {"success": False}

# 关闭
def close_socket(cli_socket):
    cli_socket.close()


if __name__ == '__main__':
    my_socket = get_server_socket()
    listen_to_client(my_socket)
    close_socket(my_socket)