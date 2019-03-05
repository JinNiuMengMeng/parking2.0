# -*- coding: utf-8 -*-
import datetime
try:
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
except:
    pass
from flask import session, request, make_response
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import get_result, param_judge, set_session, random_string, generate_md5, check_login
from appweb.plugins.handle_mysql import MysqlHelper
from config.config import PARAMS_ERROR, SESSION_HANDLE_ERROR, MYSQL_HANDLE_ERROR, USER_EXIST


@computer_web_main.route("/getuserinfo", methods=["GET", "POST"])
def get_user_info():  # 获取用户信息
    try:
        sess_key = [x for x in request.cookies.values() if len(x) == 32][0]
        user_info = session[sess_key]

        return get_result(data=user_info)
    except:
        return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 已过期, 请重新登录")


@computer_web_main.route("/login", methods=["GET", "POST"])
def login():  # 登录
    params = request.get_json()
    if param_judge(params, ["userName", "passWord"]):
        res = set_session(params)
        return res
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/logout", methods=["GET", "POST"])
def logout():  # 退出
    try:
        sess_key = request.cookies.get("token", "")
        if session.__contains__(sess_key):
            session.pop(sess_key, None)

        response = make_response(get_result(message="退出成功"))
        response.set_cookie(key="token", value="", expires=0)
        return response
    except:
        return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 删除失败")


@computer_web_main.route("/adduser", methods=["GET", "POST"])
@check_login
def add_user():  # 添加用户
    params = request.get_json()
    if param_judge(params, ["user_name", "real_name", "password", "user_role"]):
        quary_sql = """select del_flag from usr_sys_user where user_name="{}" or real_name="{}";""".format(params.get("user_name", ""), params.get("real_name", ""))
        quary_res = MysqlHelper.fetchone(quary_sql)

        salt = random_string()
        password = generate_md5(params.get("password") + salt)
        user_id = random_string()
        # 插入用户表
        if quary_res == 0:  # 不存在
            sql1 = """INSERT INTO yilu_park.usr_sys_user(id, user_type, user_name, real_name, password, salt, sex, state, del_flag, create_time, modify_time) VALUES ("{}", 1, "{}", "{}", "{}", "{}", 1, 1, 1, "{}", "{}");""".format(
                user_id, params.get("user_name"), params.get("real_name"), password, salt,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            if quary_res.get("del_flag") == 1:
                return get_result(success=False, error_code=USER_EXIST, message="用户已经存在")
            else:
                sql1 = """update yilu_park.usr_sys_user set state=1, del_flag=1, user_name="{}", real_name="{}", password="{}", salt="{}", modify_time="{}" where user_name="{}";""".format(
                    params.get("user_name"), params.get("real_name"), password, salt, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("user_name"))

        # 插入用户角色表
        quary_sql2 = """select del_flag from usr_user_role where user_id=(select id from usr_sys_user where user_name="{}");""".format(params.get("user_name"))
        quary_res2 = MysqlHelper.fetchone(quary_sql2)
        quary_role_id = """select code from usr_role where name="{}";""".format(params.get("user_role"))
        role_id = MysqlHelper.fetchone(sql=quary_role_id).get("code")

        if quary_res2 == 0:  # 不存在
            sql2 = """INSERT INTO yilu_park.usr_user_role(id, user_id, role_id, del_flag, create_time, modify_time) VALUES ("{}", "{}", "{}", 1, "{}", "{}");""".format(
                random_string(), user_id, role_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            sql2 = """update yilu_park.usr_user_role set del_flag=1, user_id="{}", role_id="{}" where role_id="{}";""".format(user_id, role_id, role_id)
        for i in [sql1, sql2]:
            res = MysqlHelper.insert(sql=i)
            if res == -1:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
            elif res == -3:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
            else:
                pass
        return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/deluser", methods=["GET", "POST"])
@check_login
def del_user():  # 删除用户
    params = request.get_json()
    if param_judge(params, ["user_id", ]):
        sql1 = """update yilu_park.usr_sys_user set state=0, del_flag=0, modify_time="{}" where id="{}";""".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("user_id"))
        sql2 = """update yilu_park.usr_user_role set del_flag=0, modify_time="{}" where user_id="{}";""".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("user_id"), )
        for i in [sql1, sql2]:
            res = MysqlHelper.insert(sql=i)
            if res == -1:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
            elif res == -3:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
            else:
                pass
        return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/getalluser", methods=["GET", "POST"])
@check_login
def get_all_user():  # 获取用户列表
    quary_sql = """SELECT id, user_name, sex, real_name, telephone, email, state, create_time from yilu_park.usr_sys_user WHERE del_flag=1;"""
    res = MysqlHelper.fetchall(sql=quary_sql)
    if res == -1:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
    elif res == -2:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
    else:
        return get_result(data=res)


