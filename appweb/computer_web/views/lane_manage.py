# -*- coding: utf-8 -*-
from flask import session
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import check_login, get_result


@computer_web_main.route("/laneRailUp", methods=["GET", "POST"])
# @check_login
def lane_rail_up():  # 抬杆
    recv_Barrier = session.get("ice_proxy")
    print(type(recv_Barrier))
    print(recv_Barrier)
    res = recv_Barrier.laneRailUp(100, 1)
    return get_result(data={"result": res})
