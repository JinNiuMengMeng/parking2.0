# -*- coding: utf-8 -*-
from flask import session, request, make_response
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import get_result, param_judge, set_session
from appweb.plugins.handle_mysql import MysqlHelper
from config.config import PARAMS_ERROR, SESSION_HANDLE_ERROR


@computer_web_main.route('/getuserinfo', methods=['GET', 'POST'])
def get_user_info():  # 获取用户信息
    try:
        user_info = session[request.cookies.values()[0]]
        return get_result(data=user_info)
    except:
        return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 已过期, 请重新登录")


@computer_web_main.route('/login', methods=['GET', 'POST'])
def login():    # 登录
    params = request.get_json()
    if param_judge(params.keys(), ['userName', 'passCode', 'passWord']):
        res = set_session(params)
        return res
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route('/logout', methods=['GET', 'POST'])
def logout():  # 退出
    try:
        if session.has_key(request.cookies.values()[0]):
            session.pop(request.cookies.values()[0], None)

        response = make_response(get_result(message="退出成功"))
        response.set_cookie(key='token', value="", expires=0)
        return response
    except:
        return get_result(success=False, error_code=SESSION_HANDLE_ERROR, message="Session 删除失败")


@computer_web_main.route('/addrole', methods=['GET', 'POST'])
def add_role():    # 添加角色
    params = request.get_json()
    if param_judge(params.keys(), ['role_name', 'parents_id', 'passWord']):
        res = set_session(params)
        return res
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")
