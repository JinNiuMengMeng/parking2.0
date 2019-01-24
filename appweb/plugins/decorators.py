# -*- coding:utf-8 -*-
import datetime
import hashlib
import json
import os
import time
from functools import wraps
from flask import abort, jsonify, make_response, session
from flask_login import current_user
from appweb.plugins.handle_mysql import MysqlHelper

from config.config import USER_PASSWORD_ERROR, USER_NOT_EXIST, MYSQL_HANDLE_ERROR


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


def get_result(data=None, success=True, error_code=0, message=None, ):
    return jsonify({"success": success, "error_code": error_code, "message": message, "data": data})


def param_judge(recv_param, regulate_param):
    recv_param.sort()
    regulate_param.sort()
    if recv_param == regulate_param:
        return True
    else:
        return False


def random_string(n=32):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(n))))[0:32]


def set_session(params):
    token_value = random_string()
    user_info = MysqlHelper.fetchone(sql="select * from station.sys_user where username=%s",
                                     params=params.get("userName"))

    if user_info == -1:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 连接失败")
    elif user_info == -2:
        return get_result(success=False, error_code=USER_NOT_EXIST, message="未找到相关用户信息")
    elif user_info == -3:
        return get_result(success=False, error_code=MYSQL_HANDLE_ERROR, message="MySQL 操作失败")

    if generate_md5(params.get("passWord", "")) == user_info.get("password", None):

        session[token_value] = {
            "username": user_info.get("username", ""),
            "user_id": user_info.get("user_id", ""),
            "password": user_info.get("password", ""),
            "rights": user_info.get("rights", ""),
            "role_id": user_info.get("role_id", ""),
            "status": user_info.get("status", ""),
            "email": user_info.get("email", ""),
            "phone": user_info.get("phone", ""),
            "user_type": user_info.get("user_type", ""),
            "cardno": user_info.get("cardno", ""),
            "sex": user_info.get("sex", ""),
            "cookies": token_value,
        }
        session.permanent = True
        response = make_response(get_result(message="登录成功"))
        out_date = datetime.datetime.now() + datetime.timedelta(hours=2)
        response.set_cookie(key='token', value=token_value, expires=out_date)
        return response
    else:
        res = get_result(success=False, error_code=USER_PASSWORD_ERROR, message="用户密码错误")
        return res
