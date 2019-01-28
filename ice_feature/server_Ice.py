# -_- coding:utf-8 -_-

import operator
import os
import shutil
import time
import requests
import Ice
import yaml

# from config.app_config import *
Ice.loadSlice("./epms.ice")
import stpy

picture_temp = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "."
                               ).split("parking2.0")[0] + "parking2.0/appweb/static/car_pic_temp"

ICE_CONFIG = ['--Ice.ThreadPool.Server.Size=5', '--Ice.ThreadPool.Server.SizeMax=10']

ST2PY_AR_ENTRANCE = 0x0003A100  # 上传入口通行记录
ST2PY_AR_EXPORT = 0x0003A200  # 出口通行记录
ST2PY_LANE_DEV_STAT = 0x0003A300  # 车道设备状态
ST2PY_LANE_WORK_STAT = 0x0003A400  # 车道工作状态

Car_Entrance = ["door_type", "car_join_time", "doorNo", "laneNo", "system_car_number",
                "identifier_car_number", "car_type", "car_status", "comment", "car_picture_path"]
Car_Export = ["door_type", "car_leave_time", "car_stay_time", "car_join_time",
              "entrance_car_number", "export_car_number", "car_type", "car_status", "comment",
              "doorNo", "laneNo", "car_picture_path"]
Lane_Dev_Stat_List = ['AuxLpr_ConnStat', 'MajLpr_ConnStat', 'ParkNO', 'RailCoilStat',
                      'RailStat', 'Rfid_ConnStat', 'SnapCoilStat', 'WorkStat', 'doorNo', 'laneNo']
Lane_Work_Stat_list = ['FreePass', 'OpenLane', 'ParkNO', 'Sleep', 'Work', 'WorkMode', 'doorNo', 'laneNo']

# 异常返回值说明
Picture_Path_Rrror = 1001           # 图片路径异常
Picture_Copy_Rrror = 1002           # 图片拷贝异常
Car_Number_identifier_Error = 2001  # 车牌号识别异常
Json_Format_Error = 3001            # Json格式异常
Command_Number_Rrror = 3002         # command 错误
Json_Field_Rrror = 3003             # Json 字段错误
User_Logout = 4001                  # 用户已退出


def get_result_json(ssID, erID=0, msg=""):
    result = """{{"sessionID": {ssID}, "errorID": {erID}, "message": "{msg}"}}
    """.format(ssID=ssID, erID=erID, msg=msg)
    return result


class Handle_stMessage(object):

    @staticmethod
    def handle_command(command, json_data, sessionID):
        if command == ST2PY_AR_ENTRANCE:
            return Handle_stMessage._car_entrance(json_data, sessionID)
        elif command == ST2PY_AR_EXPORT:
            return Handle_stMessage._car_export(json_data, sessionID)
        elif command == ST2PY_LANE_DEV_STAT:
            return Handle_stMessage._lane_dev_stat(json_data, sessionID)
        elif command == ST2PY_LANE_WORK_STAT:
            return Handle_stMessage._lane_work_stat(json_data, sessionID)
        else:
            return get_result_json(ssID=sessionID, erID=Command_Number_Rrror, msg="Command_Number_Rrror")

    @classmethod
    def _car_entrance(cls, json_data, sessionID):
        print "ar_entrance"
        oper_result = Handle_stMessage._judge_json(json_data, Car_Entrance)
        if oper_result:
            copy_picture_result = Handle_stMessage._copy_picture(json_data)
            if copy_picture_result == "success":
                for i in range(3):
                    resp = requests.get(url="http://127.0.0.1:8000/parking2/recvLaneMsg", params=json_data)
                    if resp.status_code == 200:
                        break
                    else:
                        print "发送车辆信息失败, 错误码:", resp.status_code
                return get_result_json(ssID=sessionID)
            else:
                return get_result_json(ssID=sessionID, erID=copy_picture_result, msg="Picture_Path_Rrror")
        else:
            return get_result_json(ssID=sessionID, erID=Json_Field_Rrror, msg="Json_Field_Rrror")

    @classmethod
    def _car_export(cls, json_data, sessionID):
        print "ar_export"
        oper_result = Handle_stMessage._judge_json(json_data, Car_Export)
        if oper_result:
            copy_picture_result = Handle_stMessage._copy_picture(json_data)
            if copy_picture_result == "success":
                return get_result_json(ssID=sessionID)
            else:
                return get_result_json(ssID=sessionID, erID=copy_picture_result, msg="copy_picture_result")
        else:
            return get_result_json(ssID=sessionID, erID=Json_Field_Rrror, msg="Json_Field_Rrror")

    @classmethod
    def _lane_dev_stat(cls, json_data, sessionID):
        print "lane_dev_stat"
        oper_result = Handle_stMessage._judge_json(json_data, Lane_Dev_Stat_List)

        if oper_result:
            return get_result_json(ssID=sessionID)
        else:
            return get_result_json(ssID=sessionID, erID=Json_Field_Rrror, msg="Json_Field_Rrror")

    @classmethod
    def _lane_work_stat(cls, json_data, sessionID):
        print "lane_work_stat"
        oper_result = Handle_stMessage._judge_json(json_data, Lane_Work_Stat_list)

        if oper_result:
            return get_result_json(ssID=sessionID)
        else:
            return get_result_json(ssID=sessionID, erID=Json_Field_Rrror, msg="Json_Field_Rrror")

    @classmethod
    def _copy_picture(cls, json_data):
        picture_path = json_data.get("car_picture_path", 0)
        if picture_path and json_data.has_key("car_picture_path"):
            if os.path.isfile(picture_path):
                shutil.copy(picture_path, picture_temp)
                if os.path.isfile(picture_temp + "/" + picture_path.split("/")[-1]):
                    return "success"
                else:
                    return Picture_Copy_Rrror
            else:
                return Picture_Path_Rrror
        else:
            return Picture_Path_Rrror

    @classmethod
    def _judge_json(cls, json_data, lane_list):
        lane_list.sort()
        json_data_keys_list = json_data.keys()
        json_data_keys_list.sort()
        print lane_list, ":lane_list"
        print json_data_keys_list, ":json_data_keys_list"
        return operator.eq(json_data_keys_list, lane_list)


class StPy(stpy.st2py):
    def msgSt2py(self, datajson, command, sessionID, current=None):
        print "----------- Python 站级服务端接收数据为: -----------"
        try:
            json_data = yaml.safe_load(datajson)
        except:
            return Json_Format_Error
        return Handle_stMessage.handle_command(command, json_data, sessionID)


class FakeLane(stpy.py2st):
    def msgPy2st(self, dataJson, command, sessionID, current=None):
        time.sleep(5)
        print "模拟车道服务端--接收数据为: "
        print "dataJson:\t", dataJson
        print "command:\t", command
        print "sessionID:\t", sessionID
        return sessionID


with Ice.initialize(ICE_CONFIG) as ic:  # 初始化运行环境
    adapter = ic.createObjectAdapterWithEndpoints("ssAdapter", "default -p 10000")
    py_handle = StPy()
    st_handle = FakeLane()

    adapter.add(py_handle, ic.stringToIdentity("Epms_py"))
    adapter.add(st_handle, ic.stringToIdentity("Epms_st"))

    adapter.activate()
    ic.waitForShutdown()

if __name__ == "__main__":
    # print os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")
    pass
