# -*- coding: utf-8 -*-
import datetime

from flask import request, session

from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import check_login, get_result, param_judge, random_string
from appweb.plugins.handle_mysql import MysqlHelper

from config.config import MYSQL_HANDLE_ERROR, ROLE_NAME_ERROR, PARAMS_ERROR, USER_EXIST


@computer_web_main.route("/getallrole", methods=["GET", "POST"])
@check_login
def get_all_role():  # 获取角色列表
    user_token = request.cookies.get("token")
    user_role_id = session.get(user_token).get("roleInfo").get("role_id")
    quary_sql = """SELECT code, name, state, parent_id, create_time from usr_role where del_flag=1 and parent_id="{user_role_id}" or code="{user_role_id}";""".format(user_role_id=user_role_id)
    res = MysqlHelper.fetchall(sql=quary_sql)

    # 将当前登录的用户角色的parent_id设为None(前端需求)
    for _ in res:
        if _.get("code") == user_role_id:
            _["parent_id"] = None
        else:
            pass

    # 查询当前用户角色的level(前端需求)
    res3 = MysqlHelper.fetchone(sql="""SELECT code, parent_id from usr_role where del_flag=1 and code="{}";""".format(user_role_id))
    user_parent_id = res3.get("parent_id")

    if not user_parent_id:  # parent_id 为空, 超级管理员
        level = 1
    else:
        mysql_parent_id = MysqlHelper.fetchone(sql="""SELECT code, parent_id from usr_role where del_flag=1 and code="{}";""".format(user_parent_id))
        if not mysql_parent_id.get("parent_id"):  # 根据parent_id查询对应的code与parent_id
            level = 2
        else:
            level = 3

    # 封装数据
    all_data = {
        "role_list": res,
        "role_level": level
    }

    if res == -1:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
    elif res == -2:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
    else:
        return get_result(data=all_data)


@computer_web_main.route("/addrole", methods=["GET", "POST"])
@check_login
def add_role():  # 添加角色
    params = request.get_json()
    if param_judge(params, ["name", "parent_id"]):
        role_id = code = random_string()
        find_sql = """select del_flag from yilu_park.usr_role where name="{}";""".format(params.get("name"))
        find_res = MysqlHelper.fetchone(find_sql)
        if find_res == 0:
            insert_sql = "insert yilu_park.usr_role(id, code, name, state, parent_id, del_flag, create_time) value (%s, %s, %s, %s, %s, %s, %s);"
            args = (role_id, code, params.get("name"), 1, params.get("parent_id"), 1, datetime.datetime.now())
        else:
            if find_res.get("del_flag") == 1:
                return get_result(success=False, error_code=ROLE_NAME_ERROR, message="角色名已经存在")
            else:
                insert_sql = "update yilu_park.usr_role set state=%s, parent_id=%s, del_flag=%s, delete_time=%s where name=%s;"
                args = (1, params.get("parent_id"), 1, datetime.datetime.now(), params.get("name"))
        res = MysqlHelper.insert(sql=insert_sql, params=args)
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -3:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result(data={"code": role_id})
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/delrole", methods=["GET", "POST"])
@check_login
def del_role():  # 删除角色
    params = request.get_json()
    if param_judge(params, ["role_id", ]):
        quary_sql = """select * from usr_user_role where del_flag=1 and role_id="{}";""".format(params.get("role_id"))
        res = MysqlHelper.fetchone(sql=quary_sql)
        if res != 0:
            return get_result(success=False, error_code=USER_EXIST, message="存在用户占用该角色, 不可删除")
        mysql_sql = "update yilu_park.usr_role set state=%s, del_flag=%s, delete_time=%s where code=%s;"
        res = MysqlHelper.update(sql=mysql_sql, params=(2, 0, datetime.datetime.now(), params.get("role_id")))
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -3:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/editrole", methods=["GET", "POST"])
@check_login
def edit_role():  # 修改角色
    params = request.get_json()
    if param_judge(params, ["role_id", "name"]):
        find_role = "SELECT name FROM yilu_park.usr_role WHERE code = %s and del_flag=%s;"
        res = MysqlHelper.fetchone(sql=find_role, params=(params.get("role_id"), 1))
        if res == -1 or res == -2:
            return get_result(success=False, error_code=USER_EXIST, message="不存在该角色")
        mysql_sql = "UPDATE yilu_park.usr_role SET name=%s, modify_time=%s WHERE code=%s;"
        res = MysqlHelper.insert(sql=mysql_sql, params=(params.get("name"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("role_id")))
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -3:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")
