# import requests
#
#
# if __name__ == '__main__':
#
#     data={
#         "info":{
#             "hello":"233",
#             "test":"haha",
#         }
#     }
#     requests.post("http://192.168.0.104:10000/child/sendinfo",json=data)

class testClass:
    classTemp=1
    def __init__(self):
        self.temp=1

    @classmethod
    def classMethod(cls):
        print(cls.classTemp)

    @staticmethod
    def staticMethod():
        print(233)


testInstance=testClass()
testInstance.classMethod()
testInstance.staticMethod()
print(testInstance.classTemp)


