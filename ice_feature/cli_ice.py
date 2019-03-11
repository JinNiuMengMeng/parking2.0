# -*- coding:utf-8 -*-
import os
import sys
import Ice
import yaml

Ice.loadSlice("-I%s stPython.ice"%(os.getcwd()+"/slice"))
import stpy


class StPy(stpy.st2py): # 成功返回0, 失败返回-1
    def upLaneDevStat(self, datajson, seq, current=None):
        """ 接收车道设备信息"""
        try:
            # json_data = yaml.safe_load(datajson)
            print("接收车道设备信息:", datajson, seq)
            return 0
        except:
            return -1

    def upLaneWorkstat(self, datajson, seq, current=None):
        """ 接收车道工作状态 """
        try:
            print("接收车道工作状态:", datajson, seq)
            return 0
        except:
            return -1

    def upLaneRecord(self, datajson, seq, current=None):
        """ 车辆通行记录 """
        try:
            print("车辆通行记录:", datajson, seq)
            return 0
        except:
            return -1


def py_Send_St(communicator):

    # py_send = communicator.stringToProxy("Epms_st:default  -p 9528")
    py_send = communicator.stringToProxy("Epms_st:default -h 192.168.14.137 -p 9528")
    recv_Barrier = stpy.py2stPrx.checkedCast(py_send)
    if not recv_Barrier:
        raise RuntimeError("Invalid proxy")

    # login
    adapter = communicator.createObjectAdapterWithEndpoints("xmrbi", "default")
    py_handle = StPy()
    adapter.add(py_handle, communicator.stringToIdentity("Epms_st"))
    adapter.activate()
    derived = stpy.st2pyPrx.uncheckedCast(adapter.createProxy(communicator.stringToIdentity("Epms_st")))

    res_login = recv_Barrier.login(derived, "nihao", "123")
    print("登录结果:", res_login)

    res_heart = recv_Barrier.heartBeat()
    print("心跳结果:", res_heart)

    res_lane_rail_up = recv_Barrier.laneRailUp(100, 1)
    print("抬杆结果:", res_lane_rail_up)

    res_lane_rail_down = recv_Barrier.laneRailDown(100, 1)
    print("落杆结果:", res_lane_rail_down)

    res_config_tide_lane = recv_Barrier.configTideLane(100, 1, 0)
    print("关闭潮汐车道:", res_config_tide_lane)

    res_config_tide_lane = recv_Barrier.configTideLane(100, 1, 1)
    print("打开潮汐车道:", res_config_tide_lane)

    res_upload_car_img = recv_Barrier.uploadCarImg(100, 1, 0)
    print("关闭车辆图片:", res_upload_car_img)

    res_upload_car_img = recv_Barrier.uploadCarImg(100, 1, 1)
    print("开启车辆图片:", res_upload_car_img)

    res_close_free_pass = recv_Barrier.closeFreePass(100, 1)
    print("关闭自由流:", res_close_free_pass)

    res_open_free_pass = recv_Barrier.openFreePass(100, 1)
    print("打开自由流:", res_open_free_pass)

    res_trigger_2nd_lpr = recv_Barrier.trigger2ndLpr(100, 1)
    print("触发二次车牌识别:", res_trigger_2nd_lpr)

    res_lane_sleep = recv_Barrier.laneSleep(100, 1)
    print("车道休眠:", res_lane_sleep)

    res_lane_wakeup = recv_Barrier.laneWakeup(100, 1)
    print("车道唤醒:", res_lane_wakeup)

    res_off_duty = recv_Barrier.offDuty(100, 1)
    print("车道下班:", res_off_duty)

    res_on_duty = recv_Barrier.onDuty(100, 1)
    print("车道上班:", res_on_duty)

    # res_logout = recv_Barrier.logout(derived, "nihao")
    # print("退出结果:", res_logout)

    communicator.waitForShutdown()


with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境

    py_Send_St(communicator)
