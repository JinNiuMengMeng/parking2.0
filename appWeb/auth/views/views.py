# -*- coding: utf-8 -*-
from appWeb.auth import appWeb_auth
from flask import render_template, redirect, request, url_for, flash
from appWeb.plugins.decorators import biz_logging


@appWeb_auth.before_app_request
def before_request():
    print("before_app_request")


@appWeb_auth.route('/login', methods=["GET", "POST"])
@biz_logging
def login():
    return "appWeb<br>登录页面"


@appWeb_auth.route('/logout')
def logout():
    return "appWeb<br>退出页面"


@appWeb_auth.route('/change_password')
def change_password():
    flash('您已退出')
    return redirect(url_for('appWeb_main.index'))
