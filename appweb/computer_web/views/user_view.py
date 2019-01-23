# -*- coding: utf-8 -*-
import time
from flask import session, request, Response, make_response
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import biz_logging, get_result, param_judge, random_string, set_session
from appweb.plugins.handle_mysql import MysqlHelper
from config.config import PARAMS_ERROR


@computer_web_main.route('/getuserinfo', methods=['GET', 'POST'])
def get_user_info():
    return get_result()


@computer_web_main.route('/login', methods=['GET', 'POST'])
def login():
    params = {x: (y[0] if isinstance(y, list) else y) for x, y in request.args.items()}
    if param_judge(params.keys(), ['userName', 'passCode', 'passWord']):
        res = set_session(params)
        return res["response"]
    else:
        return get_result(success=False, error_code=PARAMS_ERROR, message="参数异常")


@computer_web_main.route('/logout', methods=['GET', 'POST'])
def logout():
    res = make_response(get_result())
    res.set_cookie('name', '', expires=0)
    return res


"""
//用户信息  
router.all('/parking2/getuserinfo',function(req,res){
  res.json ({
    success: true,
    error_code: 0,
    message: null,
    data: {
    
    }
  })
})

//登陆
// 请求参数  userName,passWord,passCode
router.all('/parking2/login',function(req,res){
  res.json ({
    success: true,
    error_code: 0,
    message: null,
   
  })
})


//退出
router.all('/parking2/logout',function(req,res){
  res.json ({
    success: true,
    error_code: 0,
    message: null,
  
  })
})


"""