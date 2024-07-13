import requests
import datetime

if __name__ == '__main__':
    # print(datetime.datetime.now())
    data={
        "info":{
            "hello":"233",
            "test":"haha",
        }
    }
    requests.post("http://192.168.227.1:10000/child/sendinfo",json=data)



