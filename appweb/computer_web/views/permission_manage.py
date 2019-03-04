# -*- coding: utf-8 -*-
import datetime
import random
from flask import request
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import check_login, param_judge, get_result, random_string, make_code
from appweb.plugins.handle_mysql import MysqlHelper
from config.config import MYSQL_HANDLE_ERROR, PARAMS_ERROR, ROLE_NOT_PRI, PRI_ERROR, PRI_NUMBER


@computer_web_main.route("/getrolepri", methods=["GET", "POST"])
@check_login
def get_role_pri():  # 获取角色权限
    params = request.get_json()
    if param_judge(params, ["role_id", "parent_id"]):
        quary_sql = """SELECT privilege_code as pri_code, name as pri_name, ord_num, leaf_flag, icon, parent_code, target, remarks, url, pri_type 
                        FROM usr_grant, usr_privilege 
                        WHERE privilege_code=usr_privilege.code and usr_grant.role_id="{}";""".format(
            params.get("role_id"))

        res = MysqlHelper.fetchall(sql=quary_sql)
        if res == -2:
            res = []
        if params.get("parent_id"):
            quary_sql_parent = """SELECT privilege_code as pri_code, name as pri_name, ord_num, leaf_flag, icon, parent_code, target, remarks, url, pri_type 
                            FROM usr_grant, usr_privilege 
                            WHERE role_id="{}" 
                            and privilege_code=usr_privilege.code;""".format(params.get("parent_id"))

            parent_pri_list = MysqlHelper.fetchall(sql=quary_sql_parent)
        else:
            parent_pri_list = []
        all_res = {
            "pri_list": res,
            "parent_pri_list": parent_pri_list
        }
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -2:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result(data=all_res)
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/modifyrolepri", methods=["GET", "POST"])
@check_login
def modify_role_pri():  # 分配角色权限
    params = request.get_json()

    if param_judge(params, ["pri_codes", "role_id"]):
        # 第一步: 获取role_name的parent_name的所有权限列表
        quary_parnet_pri = """SELECT role_id, privilege_code FROM yilu_park.usr_grant WHERE role_id="{}";""".format(
            params.get("role_id"))

        quary_res = MysqlHelper.fetchall(quary_parnet_pri)

        if quary_res == -2:
            return get_result(success=False, error_code=ROLE_NOT_PRI, message="角色没有权限")
        parent_privilege_all = []
        for i in quary_res:
            parent_privilege_all.append(i.get("privilege_code"))

        # 第二步: 获取权限名称的code
        # SELECT name, code FROM yilu_park.usr_privilege WHERE name="权限管理" or name="业务管理" and del_flag=1;
        # pri_name_code_sql = """SELECT name, code FROM yilu_park.usr_privilege WHERE """
        # pri_name_list = params.get("pri_name")
        #
        # for _ in pri_name_list:
        #     if pri_name_list.index(_) + 1 == len(pri_name_list):
        #         pri_name_code_sql += 'name="' + _ + '" and del_flag=1;'
        #     else:
        #         pri_name_code_sql += 'name="' + _ + '" or '
        #
        # pri_name_code_sql_res = MysqlHelper.fetchall(pri_name_code_sql)
        # pri_name_code_list = []
        # for _ in pri_name_code_sql_res:
        #     pri_name_code_list.append(_.get("code"))

        # if len(pri_name_code_list) != len(pri_name_list):
        #     return get_result(success=False, error_code=PRI_ERROR, message="权限名错误")

        pri_name_code_list = params.get("pri_codes")

        if len(pri_name_code_list) == len(list(set(pri_name_code_list).intersection(set(parent_privilege_all)))):
            # 第三步: 判断role_name的权限是否是patent权限的子集
            # 第四步: 删除role的所有权限
            del_role_pri_sql = """DELETE FROM yilu_park.usr_grant WHERE role_id="{}";""".format(params.get("role_id"))
            MysqlHelper.insert(sql=del_role_pri_sql)
            role_id = params.get("role_id")

            # 第五步: 添加前端提交的权限
            insert_role_pri = """INSERT INTO yilu_park.usr_grant(id, role_id, privilege_code, del_flag, create_time) 
            VALUES """
            for _ in pri_name_code_list:
                if pri_name_code_list.index(_) + 1 == len(pri_name_code_list):
                    insert_role_pri += '("' + random_string() + '","' + role_id + '","' + _ + '", 1, "' + datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S") + '");'
                else:
                    insert_role_pri += '("' + random_string() + '","' + role_id + '","' + _ + '", 1, "' + datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S") + '"),'

            res = MysqlHelper.insert(sql=insert_role_pri)
            if res == -1:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
            elif res == -3:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
            else:
                return get_result()
        else:
            return get_result(success=False, error_code=PRI_ERROR, message="权限非父权限子集")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/addpri", methods=["GET", "POST"])
@check_login
def add_pri():  # 添加权限
    params = request.get_json()
    if param_judge(params,
                   ["role_id", "name", "url", "pri_type", "leaf_flag", "icon", "parent_code", "target", "remark"]):

        # 判断权限名称是否同名
        judge_name = MysqlHelper.fetchone(sql="SELECT name, code FROM yilu_park.usr_privilege WHERE name=%s;",
                                          params=(params.get("name"),))
        if judge_name:
            return get_result(success=False, message="权限名称已存在", error_code=PRI_ERROR)

        # 判断父权限id是否存在
        if params.get("parent_code"):
            judge_parent_id = MysqlHelper.fetchone(sql="SELECT name, code FROM yilu_park.usr_privilege WHERE code=%s;",
                                                   params=(params.get("parent_code"),))
            if not judge_parent_id:
                return get_result(success=False, message="parent_id不存在", error_code=PRI_ERROR)

            # 生成权限code
            find_code = MysqlHelper.fetchall(
                sql="""SELECT code FROM yilu_park.usr_privilege WHERE code LIKE "{}%";""".format(
                    params.get("parent_code")))

            code = make_code(find_code, params.get("parent_code"))
            if not code:
                return get_result(success=False, error_code=PRI_NUMBER, message="超过权限层数")
        else:
            all_code = MysqlHelper.fetchall(sql="SELECT code FROM yilu_park.usr_privilege;")
            all_code_list = [_.get("code") for _ in all_code]

            while True:
                code = str(random.randint(1000, 9999))
                if code not in all_code_list:
                    break

        # 插入数据
        insert_sql = MysqlHelper.insert(
            sql="INSERT INTO yilu_park.usr_privilege (id, code, name, pri_type, ord_num, menu_label, url, leaf_flag, icon, parent_code, remarks, target, del_flag) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
            params=(
                random_string(), code, params.get("name"), params.get("pri_type"), code, params.get("name"),
                params.get("url"), params.get("leaf_flag"), params.get("icon"), params.get("parent_code"),
                params.get("remark"), params.get("target"), 1
            ))
        if insert_sql < 0:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")

        insert_sql = MysqlHelper.insert(
            sql="INSERT INTO yilu_park.usr_grant (id, role_id, privilege_code, del_flag, creator, create_time, modifier, modify_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
            params=(random_string(), params.get("role_id"), code, 1, params.get("role_id"), datetime.datetime.now(),
                    params.get("role_id"), datetime.datetime.now()))
        if insert_sql < 0:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")

        return get_result(data={"code": code})
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/delpri", methods=["GET", "POST"])
@check_login
def del_pri():  # 删除权限
    params = request.get_json()
    if param_judge(params, ["role_id", "pri_code"]):
        sql1 = """DELETE FROM yilu_park.usr_grant WHERE privilege_code="{}" and role_id = "{}";""".format(
            params.get("pri_code"), params.get("role_id"))
        sql2 = """DELETE FROM yilu_park.usr_privilege WHERE code="{}";""".format(params.get("pri_code"))
        for i in [sql1, sql2]:
            res = MysqlHelper.insert(sql=i)
            if res < 0:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


"""
    "pri_code": pri_code,         // 权限code
    "pri_name": pri_name,         // 修改后的权限名称
    "target": null,               // 是否弹窗
    "url": "/role",
    "remark": remark              // 描述信息
"""


@computer_web_main.route("/modifypri", methods=["GET", "POST"])
@check_login
def modify_pri():  # 修改权限
    params = request.get_json()
    if param_judge(params, ["name", "url", "pri_type", "leaf_flag", "icon", "parent_code", "target", "remark"]):
        res = MysqlHelper.insert(sql="UPDATE yilu_park.usr_role SET name=%s WHERE (code=%s);",
                                 params=(params.get("pri_name"), params.get("pri_code")))
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -3:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")
