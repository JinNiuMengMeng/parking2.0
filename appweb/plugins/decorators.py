# -*- coding:utf-8 -*-
import datetime
import hashlib
import os
from functools import wraps
from flask import abort, jsonify, make_response, session,request
from flask_login import current_user
from appweb.plugins.handle_mysql import MysqlHelper

from config.config import USER_PASSWORD_ERROR, USER_NOT_EXIST, MYSQL_HANDLE_ERROR, SESSION_HANDLE_ERROR


def check_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_token = request.cookies.get("token")
        if not session.__contains__(user_token):
            return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 已过期, 请重新登录")
        return func(*args, **kwargs)
    return decorated_function


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def biz_logging(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        return func(*args, **kwargs)
    return with_logging


def generate_md5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


def get_result(data=None, success=True, error_code=0, message=None):
    return jsonify({"success": success, "error_code": error_code, "message": message, "data": data})


def param_judge(recv_param, regulate_param):
    parm_keys = list(recv_param.keys())
    parm_keys.sort()
    regulate_param.sort()
    if parm_keys == regulate_param and len(parm_keys) == len([_ for _ in recv_param.values() if _]):
        return True
    else:
        return False


def random_string(n=32):
    try:
        result = (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(n))))[0:32]
    except:
        result = (''.join(map(lambda xx: (hex(xx)[2:]), os.urandom(n))))[0:32]
    return result


def set_session(params):
    mysql_sql = """
        select usr_sys_user.id as user_id, usr_sys_user.user_name, 
          usr_sys_user.state, usr_sys_user.user_type, 
          usr_sys_user.password, usr_sys_user.salt,
          usr_user_role.role_id, usr_role.name as role_name,
          usr_grant.privilege_code as pri_code, usr_privilege.name as pri_name,
          usr_privilege.pri_type, usr_privilege.url,
          usr_privilege.parent_code, usr_privilege.leaf_flag, usr_privilege.icon, usr_privilege.target
        from usr_sys_user, usr_user_role, usr_role, usr_grant, usr_privilege
        where usr_user_role.user_id=usr_sys_user.id
          and usr_role.code=usr_user_role.role_id
          and usr_user_role.role_id=usr_grant.role_id
          and usr_grant.privilege_code=usr_privilege.code
          and usr_sys_user.user_name='{}';
    """.format(params.get("userName"))

    user_info_all = MysqlHelper.fetchall(sql=mysql_sql)
    if user_info_all == -1:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
    elif user_info_all == -2:
        return get_result(success=False, error_code=USER_NOT_EXIST, message="未找到相关用户信息")
    elif user_info_all == -3:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")

    if generate_md5(params.get("passWord", "") + user_info_all[0].get("salt", "")) == user_info_all[0].get("password", ""):
        token_value = random_string()
        privilege = []

        for user_info_one in user_info_all:
            user_info_one.pop("salt", "")
            user_info_one.pop("password", "")
            privilege.append(user_info_one)
            session[token_value] = {
                "userInfo": {
                    "user_id": user_info_one.pop("user_id", ""),
                    "user_name": user_info_one.pop("user_name", ""),
                    "state": user_info_one.pop("state", ""),
                    "user_type": user_info_one.pop("user_type", ""),
                },
                "roleInfo": {
                    "role_id": user_info_one.pop("role_id", ""),
                    "role_name": user_info_one.pop("role_name", "")
                },
                "privilegeSet": privilege,
            }

        session.permanent = True
        response = make_response(get_result(message="登录成功"))
        out_date = datetime.datetime.now() + datetime.timedelta(hours=2)
        response.set_cookie(key='token', value=token_value, expires=out_date)
        return response
    else:
        res = get_result(success=False, error_code=USER_PASSWORD_ERROR, message="用户密码错误")
        return res


if __name__ == "__main__":
    for i in range(1):
        print(random_string())


