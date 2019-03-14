# -*- coding: utf-8 -*-
from flask import request
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import get_result, param_judge, handle_func
from config.config import PARAMS_ERROR, LANE_RAIL_UP_ERROR, REQUEST_ERROR, LANE_RAIL_DOWN_ERROR, CONFIG_TIDE_LANE_ERROR, \
    UPLOAD_CAR_IMG_ERROR, OPEN_FREE_PASS_ERROR, CLOSE_FREE_PASS_ERROR, TRIGGER_2ND_LPR_ERROR, LANE_SLEEP_ERROR, \
    LANE_WAKEUP_ERROR, ON_DUTY_ERROR, OFF_DUTY_ERROR


@computer_web_main.route("/request", methods=["GET", "POST"])
def set_door_lane_request():  # 设置页面显示哪些门号道号
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):  # 传输格式待定
        res = handle_func("request", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=REQUEST_ERROR, message="设置页面显示门号道号失败")
        else:
            return get_result(success=False, error_code=REQUEST_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


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
            return get_result(success=False, error_code=LANE_RAIL_DOWN_ERROR, message="车道异常, 落杆失败")
        else:
            return get_result(success=False, error_code=LANE_RAIL_DOWN_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/configTideLane", methods=["GET", "POST"])
def config_tide_lane():  # 配置潮汐车道
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo", "onOff"]):
        res = handle_func("configTideLane", params.get("doorNo"), params.get("laneNo"), params.get("onOff"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=CONFIG_TIDE_LANE_ERROR, message="车道异常, 配置潮汐车道失败")
        else:
            return get_result(success=False, error_code=CONFIG_TIDE_LANE_ERROR, message="连接车道失败, 无法控制车道")

    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/uploadCarImg", methods=["GET", "POST", "onOff"])
def upload_car_img():   # 开启大图上传
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo", "onOff"]):
        res = handle_func("uploadCarImg", params.get("doorNo"), params.get("laneNo"), params.get("onOff"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=UPLOAD_CAR_IMG_ERROR, message="车道异常, 配置上传车辆图片失败")
        else:
            return get_result(success=False, error_code=UPLOAD_CAR_IMG_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/openFreePass", methods=["GET", "POST"])
def open_free_pass():  # 打开自由流
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("openFreePass", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=OPEN_FREE_PASS_ERROR, message="车道异常, 打开自由流接口失败")
        else:
            return get_result(success=False, error_code=OPEN_FREE_PASS_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/closeFreePass", methods=["GET", "POST"])
def close_free_pass():  # 关闭自由流
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("closeFreePass", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=CLOSE_FREE_PASS_ERROR, message="车道异常, 关闭自由流接口失败")
        else:
            return get_result(success=False, error_code=CLOSE_FREE_PASS_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/trigger2ndLpr", methods=["GET", "POST"])
def trigger_2nd_lpr():  # 触发车牌二次识别
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("trigger2ndLpr", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=TRIGGER_2ND_LPR_ERROR, message="车道异常, 车牌二次识别失败")
        else:
            return get_result(success=False, error_code=TRIGGER_2ND_LPR_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/laneSleep", methods=["GET", "POST"])
def lane_sleep():  # 车道睡眠
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("laneSleep", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=LANE_SLEEP_ERROR, message="车道异常, 配置车道睡眠失败")
        else:
            return get_result(success=False, error_code=LANE_SLEEP_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/laneWakeup", methods=["GET", "POST"])
def lane_wakeup():  # 车道唤醒
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("laneWakeup", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=LANE_WAKEUP_ERROR, message="车道异常, 车道唤醒失败")
        else:
            return get_result(success=False, error_code=LANE_WAKEUP_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/onDuty", methods=["GET", "POST"])
def on_duty():  # 车道上班
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("onDuty", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=ON_DUTY_ERROR, message="车道异常, 配置车道上班失败")
        else:
            return get_result(success=False, error_code=ON_DUTY_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/offDuty", methods=["GET", "POST"])
def off_duty():  # 车道下班
    params = request.get_json()
    if param_judge(params, ["doorNo", "laneNo"]):
        res = handle_func("offDuty", params.get("doorNo"), params.get("laneNo"))
        if res == 0:
            return get_result()
        elif res == -1:
            return get_result(success=False, error_code=OFF_DUTY_ERROR, message="车道异常, 配置车道下班失败")
        else:
            return get_result(success=False, error_code=OFF_DUTY_ERROR, message="连接车道失败, 无法控制车道")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")
