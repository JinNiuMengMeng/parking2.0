# -*- coding:utf-8 -*-


class HandleCloudMesg(object):
    """
    处理云端发送的指令
    """
    def __init__(self):
        pass

    def __repr__(self):
        return repr(self.__dict__)

    def handleMessage(self, message):
        print("接收的数据为: ", message)
