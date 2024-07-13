import BaseConfig

# PREFIX='http://' + BaseConfig.PARENT_IP + ':' + str(BaseConfig.PARENT_PORT)

API = {
    'recv': "/parent/recvinfo",
}

for item in API:
    API[item] = API[item]
