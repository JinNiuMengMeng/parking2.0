# -*- coding: utf-8 -*-
import sys
import Ice
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import check_login, get_result
from config.config import ICE_HOST, ICE_PORT
Ice.loadSlice("stPython.ice")
import stpy


@computer_web_main.route("/laneRailUp", methods=["GET", "POST"])
def lane_rail_up():  # 抬杆
    with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境
        py_send = communicator.stringToProxy("Epms_st:default -h %s -p %s" % (ICE_HOST, ICE_PORT))
        recv_barrier = stpy.py2stPrx.checkedCast(py_send)
        if not recv_barrier:
            raise RuntimeError("Invalid proxy")
        res = recv_barrier.laneRailUp(100, 1)
    return get_result(data={"result": res})


@computer_web_main.route("/heartBeat", methods=["GET", "POST"])
def heart_beat():  # 心跳
    with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境
        py_send = communicator.stringToProxy("Epms_st:default -h %s -p %s" % (ICE_HOST, ICE_PORT))
        recv_barrier = stpy.py2stPrx.checkedCast(py_send)
        if not recv_barrier:
            raise RuntimeError("Invalid proxy")
        res = recv_barrier.heartBeat()
    return get_result(data={"result": res})
