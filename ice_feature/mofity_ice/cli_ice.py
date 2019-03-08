# -*- coding:utf-8 -*-

import sys
import Ice
Ice.loadSlice("./stPython.ice")
import stpy


class StPy(stpy.st2py):
    def upLaneDevStat(self, datajson, seq, current=None):
        """ 接收车道设备信息"""
        print("----------- Python 站级服务端接收数据为: -----------")
        try:
            # json_data = yaml.safe_load(datajson)
            print(datajson)
            print(seq)
            return 1
        except:
            return 0

    def upLaneWorkstat(self, datajson, seq, current=None):
        """ 接收车道工作状态 """
        try:
            print(datajson)
            print(seq)
            return 1
        except:
            return 0


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
    print("潮汐车道:", res_config_tide_lane)

    res_upload_car_img = recv_Barrier.uploadCarImg(100, 1, 0)
    print("车辆图片:", res_upload_car_img)

    res_open_free_pass = recv_Barrier.openFreePass(100, 1)
    print("打开免费通过:", res_open_free_pass)

    res_close_free_pass = recv_Barrier.closeFreePass(100, 1)
    print("关闭免费通过:", res_close_free_pass)

    res_trigger_2nd_lpr = recv_Barrier.trigger2ndLpr(100, 1)
    print("触发二次车牌识别:", res_trigger_2nd_lpr)

    res_lane_sleep = recv_Barrier.laneSleep(100, 1)
    print("车道休眠:", res_lane_sleep)

    res_lane_wakeup = recv_Barrier.laneWakeup(100, 1)
    print("车道唤醒:", res_lane_wakeup)

    res_on_duty = recv_Barrier.onDuty(100, 1)
    print("车道上班:", res_on_duty)

    res_off_duty = recv_Barrier.offDuty(100, 1)
    print("车道下班:", res_off_duty)

    # res_logout = recv_Barrier.logout(derived, "nihao")
    # print("退出结果:", res_logout)

    communicator.waitForShutdown()


with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境

    py_Send_St(communicator)
