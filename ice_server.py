# -*- coding:utf-8 -*-
import os
import sys
import Ice
import yaml
Ice.loadSlice("-I%s stPython.ice" % (os.getcwd() + "/slice"))
import stpy


def get_result_ice(Result, Sequence, Expand):
    return """{{"Result": {}, "Sequence": {}, "Expand": "{}"}}""".format(Result, Sequence, Expand)


class StPy(stpy.st2py):  # 成功返回0, 失败返回-1
    def upLaneDevStat(self, datajson, seq, current=None):
        """ 接收车道设备信息"""
        try:
            json_data = yaml.safe_load(datajson)
            result = get_result_ice(Result=0, Sequence=seq, Expand="")

            print("接收车道设备信息:", json_data, seq)
            print("返回数据:", result, seq)
            return result
        except:
            result = get_result_ice(Result=-1, Sequence=seq, Expand="Json解析失败, 请检查格式")
            print("返回数据:", result, seq)
            return result

    def upLaneWorkstat(self, datajson, seq, current=None):
        """ 接收车道工作状态 """
        try:
            json_data = yaml.safe_load(datajson)
            result = get_result_ice(Result=0, Sequence=seq, Expand="")

            print("接收车道工作状态", json_data, seq)
            print("返回数据:", get_result_ice(Result=0, Sequence=seq, Expand=""), seq)
            return result
        except:
            result = get_result_ice(Result=-1, Sequence=seq, Expand="Json解析失败, 请检查格式")
            print("返回数据:", get_result_ice(Result=-1, Sequence=seq, Expand="Json解析失败, 请检查格式"), seq)
            return result

    def upLaneRecord(self, datajson, seq, current=None):
        """ 车辆通行记录 """
        try:
            json_data = yaml.safe_load(datajson)
            result = get_result_ice(Result=0, Sequence=seq, Expand="")
            print("车辆通行记录:", json_data, seq)
            return result
        except:
            result = get_result_ice(Result=-1, Sequence=seq, Expand="Json解析失败, 请检查格式")
            return result


if __name__ == "__main__":

    communicator = Ice.initialize(sys.argv)  # 初始化运行环境
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
    res_login = recv_Barrier.login(derived, "python_station", "123")
    print("登录结果:", res_login)
    communicator.waitForShutdown()
