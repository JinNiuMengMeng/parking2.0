# -*- coding:utf-8 -*-

import sys
import Ice

Ice.loadSlice("./epms.ice")
import stpy


def st_Send_Py(communicator):
    ST2PY_AR_ENTRANCE = 0x0003A100  # 上传入口通行记录
    ST2PY_AR_EXPORT = 0x0003A200  # 出口通行记录
    ST2PY_LANE_DEV_STAT = 0x0003A300  # 车道设备状态
    ST2PY_LANE_WORK_STAT = 0x0003A400  # 车道工作状态

    send_data_1 = """{"door_type": "Entrance","car_join_time": "2018-11-11 10:00:00","doorNo": "2","laneNo": "1","system_car_number": "闽DZ11223","identifier_car_number": "闽DZ11223","car_type": "临时车辆","car_status": "","comment": "","car_picture_path": "/home/ubuntu/Pictures/girl.jpg"}"""
    send_data_2 = """{"door_type": "Export", "car_leave_time": "2018-11-11 12:00:00", "car_stay_time": "2时00分", "car_join_time": "2018-11-11 10:00:00", "entrance_car_number": "闽DZ11223", "export_car_number": "闽DZ11223", "car_type": "临时车辆", "car_status": "", "comment": "", "doorNo": "2", "laneNo": "1", "car_picture_path": "/home/ubuntu/Pictures/Screenshot.png"}"""
    send_data_3 = """{"doorNo": "2","laneNo": "1","SnapCoilStat": "0","RailCoilStat": "1","RailStat": "0","Rfid_ConnStat": "1","MajLpr_ConnStat": "1","WorkStat": "0","AuxLpr_ConnStat": "0","ParkNO": "3967968933467"}"""
    send_data_4 = """{"doorNo": "2","laneNo": "1","Work": "0","OpenLane": "1","FreePass": "0","Sleep": "1","WorkMode": "1","ParkNO": "3967968933467"}"""

    st_send = communicator.stringToProxy("Epms_py:default -p 10000").ice_twoway().ice_timeout(200).ice_secure(False)
    send_Lane = stpy.st2pyPrx.checkedCast(st_send.ice_timeout(200))
    if not send_Lane:
        raise RuntimeError("Invalid proxy")

    res_ar_entrance = send_Lane.msgSt2py(send_data_1, ST2PY_AR_ENTRANCE, 10)
    print("res_ar_entrance:", res_ar_entrance)
    # time.sleep(1)

    res_ar_export = send_Lane.msgSt2py(send_data_2, ST2PY_AR_EXPORT, 11)
    print("res_ar_export:", res_ar_export)
    # time.sleep(1)

    res_lane_dev_stat = send_Lane.msgSt2py(send_data_3, ST2PY_LANE_DEV_STAT, 12)
    print("res_lane_dev_stat:", res_lane_dev_stat)
    # time.sleep(1)

    res_lane_work_stat = send_Lane.msgSt2py(send_data_4, ST2PY_LANE_WORK_STAT, 13)
    print("res_lane_work_stat:", res_lane_work_stat)
    # time.sleep(1)


def py_Send_St(communicator):
    send_data_1 = '{"doorNo": 1,"laneNo": 2}'
    send_data_2 = '{"doorNo": 1,"laneNo": 2, "status": 1}'
    send_data_3 = '{"doorNo": 1,"laneNo": 2, "status": 0}'
    PY2ST_RAIL_UP = 0x0004A100  # 抬杆
    PY2ST_RAIL_DOWN = 0x0004A200  # 落杆
    PY2ST_OPEN_TIDE_LANE = 0x0004A300  # 打开潮汐车道
    PY2ST_UPLOAD_CAR_IMG = 0x0004A400  # 是否长传图片
    PY2ST_UPLOAD_DOORNO_LANE_INFO = 0x0004A500  # 上传门号道号信息

    PY2ST_CONFIG_COMMON_LANETYPE = 0x0004A700  # 一车一杆
    PY2ST_CONFIG_FREEPASS = 0x0004A800  # 自由流
    PY2ST_CONFIG_LANESLEEP = 0x0004A900  # 车道唤醒，休眠
    PY2ST_TRIGGER_2ND_LPR = 0x0004AA00  # 二次识别
    PY2ST_CONFIG_SYSTEM_ON_DUTY = 0x0004AB00  # 上下班

    py_send = communicator.stringToProxy("Epms_st:default -p 10000")
    recv_Barrier = stpy.py2stPrx.checkedCast(py_send)
    if not recv_Barrier:
        raise RuntimeError("Invalid proxy")

    # 抬杆
    res_rall_up = recv_Barrier.msgPy2st(send_data_1, PY2ST_RAIL_UP, 1)
    print("res_rall_up:", res_rall_up)

    # 落杆
    res_rall_down = recv_Barrier.msgPy2st(send_data_1, PY2ST_RAIL_DOWN, 2)
    print("res_rall_down:", res_rall_down)

    # 打开潮汐车道
    res_tide_lane = recv_Barrier.msgPy2st(send_data_2, PY2ST_OPEN_TIDE_LANE, 3)
    print("res_tide_lane:", res_tide_lane)

    # 是否长传图片
    res_car_img = recv_Barrier.msgPy2st(send_data_2, PY2ST_UPLOAD_CAR_IMG, 4)
    print("res_car_img:", res_car_img)

    # 上传门号道号信息
    res_doorNo_lane_info = recv_Barrier.msgPy2st(send_data_2, PY2ST_UPLOAD_DOORNO_LANE_INFO, 5)
    print("res_doorNo_lane_info:", res_doorNo_lane_info)

    # 一车一杆
    res_laneType = recv_Barrier.msgPy2st(send_data_2, PY2ST_CONFIG_COMMON_LANETYPE, 6)
    print("res_laneType:", res_laneType)

    # 自由流
    res_freepass = recv_Barrier.msgPy2st(send_data_2, PY2ST_CONFIG_FREEPASS, 7)
    print("res_freepass:", res_freepass)

    # 车道唤醒，休眠
    res_laneSleep = recv_Barrier.msgPy2st(send_data_2, PY2ST_CONFIG_LANESLEEP, 8)
    print("res_laneSleep:", res_laneSleep)

    # 二次识别
    res_trigger = recv_Barrier.msgPy2st(send_data_2, PY2ST_TRIGGER_2ND_LPR, 9)
    print("res_trigger:", res_trigger)

    # 上下班
    res_on_duty = recv_Barrier.msgPy2st(send_data_2, PY2ST_CONFIG_SYSTEM_ON_DUTY, 10)
    print("res_on_duty:", res_on_duty)


with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境

    # py_Send_St(communicator)
    st_Send_Py(communicator)
