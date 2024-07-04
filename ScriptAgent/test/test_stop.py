import requests

if __name__ == '__main__':
    data={
        "command": "mynettest",
        "arguments": [{"end":20},{"numbers":[30,40,50]}],
        "pattern": "/pattern01",
        "power": ""
    }
    res=requests.post("http://127.0.0.1:10002/script/stopscript", json=data)






