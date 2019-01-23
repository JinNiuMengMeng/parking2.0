# -*- coding:utf-8 -*-
import datetime
import os
from functools import wraps
from flask import abort, jsonify, session, Response, make_response, request
from flask_login import current_user
from appweb.plugins.handle_mysql import MysqlHelper
from werkzeug.http import parse_cookie


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

"""
    response=make_response('Hello World');  
    response.set_cookie('Name','Hyman')  
    return response
    
    response.headers.add('No-Cookie', parse_cookie(response.headers.get('Set-Cookie'))[app.session_cookie_name])
    response.headers.remove('Set-Cookie')
"""


def set_session(params):
    token_value = random_string()
    user_info = MysqlHelper.fetchone(sql="select * from station.sys_user where username=%s",
                                     params=params.get("userName"))
    session[token_value] = {}
    session[token_value]["userName"] = params.get("userName", None)
    session[token_value]["user_id"] = user_info.get("user_id", None)
    session[token_value]["passWord"] = user_info.get("password", None)
    session[token_value]["rights"] = user_info.get("rights", None)
    session[token_value]["role_id"] = user_info.get("role_id", None)
    session[token_value]["status"] = user_info.get("status", None)
    session[token_value]["email"] = user_info.get("email", None)
    session[token_value]["phone"] = user_info.get("phone", None)
    session[token_value]["user_type"] = user_info.get("user_type", None)
    session[token_value]["cardno"] = user_info.get("cardno", None)
    session[token_value]["sex"] = user_info.get("sex", None)

    res = make_response(get_result())

    out_date = datetime.datetime.now() + datetime.timedelta(hours=2)
    res.set_cookie(key='token', value=token_value,  expires=out_date)

    # res.headers["token"] = random_cookies + "; HttpOnly; Path=/"
    return {"response": res, "session": session}
