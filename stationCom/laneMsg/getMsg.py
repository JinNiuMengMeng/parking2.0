# -*- coding:utf-8 -*-

import zmq
from stationCom.config import HOST, PORT
from stationCom.laneMsg.handleMsg import handleMessage


def getLaneMsg():
    """
    订阅车道传递的消息
    :return:
    """
    context = zmq.Context()
    recviver = context.socket(zmq.PULL)
    recviver.connect("tcp://" + HOST + ":" + str(PORT))
    print("消息订阅已启动")
    while True:
        msg = recviver.recv_string()
        handleMessage(message=msg)
