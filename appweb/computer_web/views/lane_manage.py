# -*- coding: utf-8 -*-
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import check_login, get_result, cli_ice


@computer_web_main.route("/laneRailUp", methods=["GET", "POST"])
def lane_rail_up():  # 抬杆
    res = cli_ice.laneRailUp(100, 1)
    return get_result(data={"result": res})


@computer_web_main.route("/heartBeat", methods=["GET", "POST"])
def heart_beat():  # 心跳
    res = cli_ice.heartBeat()
    return get_result(data={"result": res})
