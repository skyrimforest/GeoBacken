import BaseConfig

PREFIX='http://' + BaseConfig.PARENT_IP + ':' + str(BaseConfig.PARENT_PORT)

API={
    'register': '/child/register'
}

for item in API:
    API[item]=PREFIX+API[item]