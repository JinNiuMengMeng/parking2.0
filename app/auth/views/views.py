# -*- coding: utf-8 -*-

from app.auth import auth

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from app.main.forms.baseforms import LoginForm
from app.model.SysUser import SysUser
from app.plugins.decorators import biz_logging


@auth.before_app_request
def before_request():
    print("before_app_request")


@auth.route('/login', methods=["GET", "POST"])
@biz_logging
def login():
    logout_user()
    form = LoginForm()
    print(form)
    if form.validate_on_submit():
        user = SysUser.query.filter_by(userName=form.userName.data).first()
        if(user is not None) and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            print("登录成功")
            return redirect(request.args.get('next') or url_for("main.index"))
        flash("无效的用户名或密码")
    return render_template("auth/login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出')
    return redirect(url_for('main.index'))


@auth.route('/change_password')
@login_required
def change_password():
    flash('您已退出')
    return redirect(url_for('main.index'))