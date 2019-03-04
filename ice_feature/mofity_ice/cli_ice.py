# -*- coding:utf-8 -*-

import sys
import Ice
import yaml

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
        except:
            return 0
        return 1

    def upLaneWorkstat(self, datajson, seq, current=None):
        """ 接收车道工作状态 """
        print(datajson)
        print(seq)
        return 1


def py_Send_St(communicator):
    send_data_1 = '{"doorNo": 1,"laneNo": 2}'

    py_send = communicator.stringToProxy("Epms_st:default -p 10000")
    recv_Barrier = stpy.py2stPrx.checkedCast(py_send)
    if not recv_Barrier:
        raise RuntimeError("Invalid proxy")

    # login
    adapter = communicator.createObjectAdapterWithEndpoints("ssAdapter", "default")
    py_handle = StPy()

    adapter.add(py_handle, communicator.stringToIdentity("Epms_py"))
    adapter.activate()

    derived = stpy.st2pyPrx.uncheckedCast(adapter.createProxy(communicator.stringToIdentity("Epms_py")))

    res_login = recv_Barrier.login(derived, "nihao", "123")
    print(res_login)
    communicator.waitForShutdown()





'''
    # 抬杆
    # 落杆
    # 打开潮汐车道
    # 是否长传图片
    # 上传门号道号信息
    # 一车一杆
    # 自由流
    # 车道唤醒，休眠
    # 二次识别
    # 上下班
'''


with Ice.initialize(sys.argv) as communicator:  # 初始化运行环境

    py_Send_St(communicator)
