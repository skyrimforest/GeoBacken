import requests

if __name__ == '__main__':
    data = {
        "command": "mytest",
        "arguments": [""]
    }
    requests.post("http://127.0.0.1:10000/script/runscript", json=data)
