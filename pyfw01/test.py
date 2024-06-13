import requests


if __name__ == '__main__':

    data={
        "info":{
            "hello":"233",
            "test":"haha",
        }
    }
    requests.post("http://192.168.0.104:10000/child/sendinfo",json=data)
