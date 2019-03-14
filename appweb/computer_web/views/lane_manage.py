# -*- coding: utf-8 -*-
from flask import request
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import get_result, param_judge, handle_func
from config.config import PARAMS_ERROR, LANE_RAIL_UP_ERROR


@computer_web_main.route("/laneRailUp", methods=["GET", "POST"])
def lane_rail_up():  # 抬杆
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("laneRailUp", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=LANE_RAIL_UP_ERROR, message="车道异常, 抬杆失败")
        else:
            return get_result(success=False, error_code=LANE_RAIL_UP_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/laneRailDown", methods=["GET", "POST"])
def lane_rail_down():  # 落杆
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("laneRailDown", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=LANE_RAIL_UP_ERROR, message="车道异常, 抬杆失败")
        else:
            return get_result(success=False, error_code=LANE_RAIL_UP_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/configTideLane", methods=["GET", "POST"])
def config_tide_lane():  # 配置潮汐车道
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo", "onOff"]):
        res = handle_func("configTideLane", params.get("doorNo"), params.get("laneNo"), params.get("onOff"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/uploadCarImg", methods=["GET", "POST", "onOff"])
def upload_car_img():   # 开启大图上传
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo", "onOff"]):
        res = handle_func("uploadCarImg", params.get("doorNo"), params.get("laneNo"), params.get("onOff"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/openFreePass", methods=["GET", "POST"])
def open_free_pass():  # 打开自由流
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("openFreePass", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/closeFreePass", methods=["GET", "POST"])
def close_free_pass():  # 关闭自由流
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("closeFreePass", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/trigger2ndLpr", methods=["GET", "POST"])
def trigger_2nd_lpr():  # 触发车牌二次识别
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("trigger2ndLpr", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/laneSleep", methods=["GET", "POST"])
def lane_sleep():  # 车道睡眠
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("laneSleep", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/laneWakeup", methods=["GET", "POST"])
def lane_wakeup():  # 车道唤醒
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("laneWakeup", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/onDuty", methods=["GET", "POST"])
def on_duty():  # 车道上班
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("onDuty", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/offDuty", methods=["GET", "POST"])
def off_duty():  # 车道下班
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("offDuty", params.get("doorNo"), params.get("laneNo"))
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")
