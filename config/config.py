# -*- coding:utf-8 -*-

# command 指令
ST2PY_AR_ENTRANCE = 0x0003A100                  # 上传入口通行记录
ST2PY_AR_EXPORT = 0x0003A200                    # 出口通行记录
ST2PY_LANE_DEV_STAT = 0x0003A300                # 车道设备状态
ST2PY_LANE_WORK_STAT = 0x0003A400               # 车道工作状态

PY2ST_RAIL_UP = 0x0004A100                      # 抬杆
PY2ST_RAIL_DOWN = 0x0004A200                    # 落杆
PY2ST_OPEN_TIDE_LANE = 0x0004A300               # 打开潮汐车道
PY2ST_UPLOAD_CAR_IMG = 0x0004A400               # 是否长传图片
PY2ST_UPLOAD_DOORNO_LANE_INFO = 0x0004A500      # 上传门号道号信息

PY2ST_CONFIG_COMMON_LANETYPE = 0x0004A700	    # 一车一杆
PY2ST_CONFIG_FREEPASS = 0x0004A800	            # 自由流
PY2ST_CONFIG_LANESLEEP = 0x0004A900	            # 车道唤醒，休眠
PY2ST_TRIGGER_2ND_LPR = 0x0004AA00	            # 二次识别
PY2ST_CONFIG_SYSTEM_ON_DUTY = 0x0004AB00        # 上下班


Car_Entrance = [                # 车辆出口字段
    "door_type",                # 进入口类型, 入口
    "car_join_time",            # 车辆入场时间
    "doorNo",                   # 门号
    "laneNo",                   # 道号
    "system_car_number",        # 系统车牌
    "identifier_car_number",    # 识别车牌
    "car_type",                 # 车辆类型
    "car_status",               # 状态
    "comment",                  # 备注
    "car_picture_path",         # 车辆图片路径+图片名 "/root/picture/图片名.png"
]

Car_Export = [                # 车辆入口字段
    "door_type",              # 进入口类型, 出口
    "car_leave_time",         # 车辆出场时间
    "car_stay_time",          # 车辆停留时间
    "car_join_time",          # 车辆入场时间
    "entrance_car_number",    # 入口车号
    "export_car_number",      # 出口车号
    "car_type",               # 车辆类型
    "car_status",             # 状态
    "comment",                # 备注
    "doorNo",                 # 门号
    "laneNo",                 # 道号
    "car_picture_path",       # 车辆图片路径+图片名 "/root/picture/图片名.png"
]
Lane_Dev_Stat_List = [      # 车道设备状态
    "doorNo",               # 门号
    "laneNo",               # 道号
    "SnapCoilStat",         # 抓拍线圈状态 -> 前地
    "RailCoilStat",         # 栏杆线圈状态 -> 后地
    "RailStat",             # 栏杆状态
    "Rfid_ConnStat",        # RFID天线状态
    "MajLpr_ConnStat",      # 双车牌主车牌 -> 识别一
    "WorkStat",             # 工作状态
    "AuxLpr_ConnStat",      # 双车牌辅车牌 -> 识别二
    "ParkNO",               # 车场编号
]

Lane_Work_Stat_list = [    # 车道工作状态
    "doorNo",       # 门号
    "laneNo",       # 道号
    "Work",         # 上下班
    "OpenLane",     # 开启车道
    "FreePass",     # 自由流
    "Sleep",        # 车道睡眠-潮汐车道
    "WorkMode",     # 车道工作模式
    "ParkNO",       # 车道编号
]


# 异常返回值说明 ICE
Picture_Path_Rrror = 1001           # 图片路径异常
Picture_Copy_Rrror = 1002           # 图片拷贝异常
Car_Number_identifier_Error = 2001  # 车牌号识别异常
Json_Format_Error = 3001            # Json格式异常
Command_Number_Rrror = 3002         # command 错误
Json_Field_Rrror = 3003             # Json 字段错误

# 前端
PARAMS_ERROR = 10001                # 参数异常
USER_PASSWORD_ERROR = 20001         # 密码错误
USER_NOT_EXIST = 20002              # 用户名错误或者用户不存在

REDIS_HANDLE_ERROR = 30001          # Redis 操作失败
MYSQL_HANDLE_ERROR = 30002          # Mysql 操作失败
SESSION_HANDLE_ERROR = 30003        # Session 过期
USER_LOGIN_ERROR = 40000            # 用户登录异常
USER_LOGOUT = 40001                 # 用户退出
USER_EXIST = 40002                  # 用户已经存在

ROLE_NAME_ERROR = 40003             # 角色名已经存在
ROLE_NOT_PRI = 40004                # 角色没有权限

PRI_ERROR = 50001                   # 权限名错误
PRI_NUMBER = 50002                  # 超过权限层数
