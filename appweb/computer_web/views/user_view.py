# -*- coding: utf-8 -*-
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import session, request, make_response
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import get_result, param_judge, set_session, random_string, generate_md5
from appweb.plugins.handle_mysql import MysqlHelper
from config.config import PARAMS_ERROR, SESSION_HANDLE_ERROR, MYSQL_HANDLE_ERROR, ROLE_NAME_ERROR, USER_EXIST, \
    ROLE_NOT_PRI, PRI_ERROR


@computer_web_main.route("/getuserinfo", methods=["GET", "POST"])
def get_user_info():  # 获取用户信息
    try:
        user_info = session[request.cookies.values()[0]]
        return get_result(data=user_info)
    except:
        return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 已过期, 请重新登录")


@computer_web_main.route("/login", methods=["GET", "POST"])
def login():    # 登录
    params = request.get_json()
    if param_judge(params, ["userName", "passCode", "passWord"]):
        res = set_session(params)
        return res
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/logout", methods=["GET", "POST"])
def logout():  # 退出
    try:
        if session.has_key(request.cookies.values()[0]):
            session.pop(request.cookies.values()[0], None)

        response = make_response(get_result(message="退出成功"))
        response.set_cookie(key="token", value="", expires=0)
        return response
    except:
        return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 删除失败")


@computer_web_main.route("/addrole", methods=["GET", "POST"])
def add_role():    # 添加角色
    params = request.get_json()
    if param_judge(params, ["name", "parent_id"]):
        role_id = code = random_string()
        find_sql = """select del_flag from yilu_park.usr_role where name="{}";""".format(params.get("name"))
        find_res = MysqlHelper.fetchone(find_sql)
        if find_res == 0:
            insert_sql = """insert yilu_park.usr_role(id, code, name, state, parent_id, del_flag, create_time) 
            value("{}", "{}", "{}", 1, "{}", 1, "{}");
            """.format(role_id, code, params.get("name"), params.get("parent_id"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            if find_res.get("del_flag") == 1:
                return get_result(success=False, error_code=ROLE_NAME_ERROR, message="角色名已经存在")
            else:
                insert_sql = """update yilu_park.usr_role set state=1, parent_id="{}", del_flag=1, delete_time="{}"
                                where name="{}";""".format(params.get("parent_id"),
                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("name"))
        res = MysqlHelper.insert(sql=insert_sql)
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -3:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/delrole", methods=["GET", "POST"])
def del_role():    # 删除角色
    params = request.get_json()
    if param_judge(params, ["role_name", ]):
        quary_sql = """select * from usr_user_role where del_flag=1 and role_id=(select id from usr_role where name="{}");""".format(
            params.get("role_name")
        )
        res = MysqlHelper.fetchone(sql=quary_sql)
        if res != 0:
            return get_result(success=False, error_code=USER_EXIST, message="存在用户占用该角色, 不可删除")

        mysql_sql = """update yilu_park.usr_role set state={}, del_flag={}, delete_time="{}" where name="{}";""".format(
            2, 0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("role_name"))

        res = MysqlHelper.update(sql=mysql_sql)
        if res == -1:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
        elif res == -3:
            return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
        else:
            return get_result()
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/modifypri", methods=["GET", "POST"])
def modify_role_pri():    # 修改角色权限
    params = request.get_json()

    if param_judge(params, ["pri_name", "role_name"]):
        """
-- 修改角色权限  "role_name", "pri_name": ["权限管理", "业务管理"]
-- 第一步: 获取role_name的parent_name的所有权限列表
SELECT role_id, privilege_code 
FROM yilu_park.usr_grant 
WHERE role_id=(SELECT parent_id FROM yilu_park.usr_role WHERE name="岗亭人员" and del_flag=1) and del_flag=1;

-- 第二步: 获取权限名称的code
SELECT name, code FROM yilu_park.usr_privilege WHERE name="权限管理" or name="业务管理" and del_flag=1;

-- 第三步: 代码判断code是否全部存在于parent_name的权限列表中
-- 第四步: 删除有关role_name的所有权限
-- INSERT INTO hk_test(username, passwd) VALUES ('qmf2', 'qmf2'),('qmf3', 'qmf3'),('qmf4', 'qmf4'),('qmf5', 'qmf5')
DELETE FROM yilu_park.usr_grant WHERE role_id=(SELECT code FROM yilu_park.usr_role WHERE name="岗亭人员" and del_flag=1);
-- 第五步: 添加前端提交的所有记录
INSERT INTO yilu_park.usr_grant(id, role_id, privilege_code, del_flag, create_time, modify_time) 
VALUES (),(),()
        """
        # 第一步: 获取role_name的parent_name的所有权限列表
        quary_parnet_pri = """SELECT role_id, privilege_code FROM yilu_park.usr_grant WHERE role_id=(SELECT parent_id 
              FROM yilu_park.usr_role WHERE name="{}" and del_flag=1) and del_flag=1;""".format(params.get("role_name"))

        quary_res = MysqlHelper.fetchall(quary_parnet_pri)

        if quary_res == -2:
            return get_result(success=False, error_code=ROLE_NOT_PRI, message="角色没有权限")
        parent_privilege_all = []
        for i in quary_res:
            parent_privilege_all.append(i.get("privilege_code"))

        # 第二步: 获取权限名称的code
        # SELECT name, code FROM yilu_park.usr_privilege WHERE name="权限管理" or name="业务管理" and del_flag=1;
        pri_name_code_sql = """SELECT name, code FROM yilu_park.usr_privilege WHERE """
        pri_name_list = params.get("pri_name")

        for _ in pri_name_list:
            if pri_name_list.index(_) + 1 == len(pri_name_list):
                pri_name_code_sql += 'name="' + _ + '" and del_flag=1;'
            else:
                pri_name_code_sql += 'name="' + _ + '" or '

        pri_name_code_sql_res = MysqlHelper.fetchall(pri_name_code_sql)
        pri_name_code_list = []
        for _ in pri_name_code_sql_res:
            pri_name_code_list.append(_.get("code"))

        if len(pri_name_code_list) != len(pri_name_list):
            return get_result(success=False, error_code=PRI_ERROR, message="权限名错误")

        if len(pri_name_code_list) == len(list(set(pri_name_code_list).intersection(set(parent_privilege_all)))):
            # 判断role_name的权限是否是patent权限的子集
            # 删除role的所有权限
            del_role_pri_sql = """DELETE FROM yilu_park.usr_grant WHERE role_id=(SELECT code FROM yilu_park.usr_role 
                WHERE name="{}" and del_flag=1);""".format(params.get("role_name"))
            MysqlHelper.insert(sql=del_role_pri_sql)
            role_id = MysqlHelper.fetchone(sql="""SELECT code FROM yilu_park.usr_role WHERE name="{}" and del_flag=1""".format(params.get("role_name"))).get("code")

            # 添加权限
            insert_role_pri = """INSERT INTO yilu_park.usr_grant(id, role_id, privilege_code, del_flag, create_time) 
            VALUES """
            for _ in pri_name_code_list:
                if pri_name_code_list.index(_) + 1 == len(pri_name_code_list):
                    insert_role_pri += '("' + random_string() + '","' + role_id + '","' + _ + '", 1, "' + datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S") + '");'
                else:
                    insert_role_pri += '("' + random_string() + '","' + role_id + '","' + _ + '", 1, "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '"),'

            res = MysqlHelper.insert(sql=insert_role_pri)
            if res == -1:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
            elif res == -3:
                return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")
            else:
                return get_result()
        else:
            return get_result(success=False, error_code=PRI_ERROR, message="权限名错误")
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route("/adduser", methods=["GET", "POST"])
def add_user():    # 添加用户
    params = request.get_json()
    if param_judge(params, ["user_name", "real_name", "password", "user_role"]):
        quary_sql = """select del_flag from usr_sys_user where user_name="{}" or real_name="{}";""".format(
            params.get("user_name", ""), params.get("real_name", ""))
        quary_res = MysqlHelper.fetchone(quary_sql)

        salt = random_string()
        password = generate_md5(params.get("password") + salt)
        user_id = random_string()
        # 插入用户表
        if quary_res == 0:  # 不存在
            sql1 = """INSERT INTO yilu_park.usr_sys_user(id, user_type, user_name, real_name, password, salt, sex, state, 
                del_flag, create_time, modify_time) VALUES ("{}", 1, "{}", "{}", "{}", "{}", 1, 1, 1, "{}", "{}");""".format(
                user_id, params.get("user_name"), params.get("real_name"), password, salt,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            if quary_res.get("del_flag") == 1:
                return get_result(success=False, error_code=USER_EXIST, message="用户已经存在")
            else:
                sql1 = """update yilu_park.usr_sys_user set state=1, del_flag=1, user_name="{}", real_name="{}", 
                        password="{}", salt="{}", modify_time="{}" where user_name="{}";""".format(params.get("user_name"),
                        params.get("real_name"), password, salt, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        params.get("user_name"))

        # 插入用户角色表
        quary_sql2 = """select del_flag from usr_user_role where user_id=(select id from usr_sys_user where user_name="{}");""".format(
            params.get("user_name"))

        quary_res2 = MysqlHelper.fetchone(quary_sql2)
        quary_role_id = """select code from usr_role where name="{}";""".format(params.get("user_role"))
        role_id = MysqlHelper.fetchone(sql=quary_role_id).get("code")

        if quary_res2 == 0:  # 不存在
            sql2 = """INSERT INTO yilu_park.usr_user_role(id, user_id, role_id, del_flag, create_time, modify_time) 
                      VALUES ("{}", "{}", "{}", 1, "{}", "{}");""".format(
                random_string(), user_id, role_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            sql2 = """update yilu_park.usr_user_role set del_flag=1, user_id="{}", role_id="{}" where role_id="{}";""".format(
                user_id, role_id, role_id)

        for i in [sql1, sql2]:
            print i
            res = MysqlHelper.insert(sql=i)
            print res
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
def del_user():    # 删除用户
    params = request.get_json()
    if param_judge(params, ["user_name", ]):
        sql1 = """update yilu_park.usr_sys_user set state=0, del_flag=0, modify_time="{}" where user_name="{}";""".format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("user_name"))
        sql2 = """update yilu_park.usr_user_role set del_flag=0, modify_time="{}" where user_id=
              (select id from usr_sys_user where user_name="{}");""".format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), params.get("user_name"),)
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
