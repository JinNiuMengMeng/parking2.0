# -*- coding: utf-8 -*-
import sys
import Ice
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import check_login, get_result
Ice.loadSlice("ice_feature/mofity_ice/cli_ice.py")
import stpy


@computer_web_main.route("/laneRailUp", methods=["GET", "POST"])
# @check_login
def lane_rail_up():  # 抬杆
    with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境
        py_send = communicator.stringToProxy("Epms_st:default -h 192.168.14.137 -p 9528")
        recv_Barrier = stpy.py2stPrx.checkedCast(py_send)
        if not recv_Barrier:
            raise RuntimeError("Invalid proxy")
    res = recv_Barrier.laneRailUp(100, 1)
    return get_result(data={"result": res})

