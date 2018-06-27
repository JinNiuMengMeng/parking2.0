# -*- coding:utf-8 -*-

import zmq
from stationCom.laneMsg.handleMsg import HandleLaneMesg


class GetLaneMesg(object):
    """
    获取车道消息 - zmq订阅端
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def getLaneMsg(self):
        """
        接收车道传递来的消息
        """
        context = zmq.Context()
        recviver = context.socket(zmq.PULL)
        recviver.connect("tcp://%s:%d" % (self.host, self.port))
        print("处于订阅状态...")
        while True:
            msg = recviver.recv_string()
            HandleLaneMesg().handleMessage(message=msg)



