from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from app.main import main

from app.model.SysUser import Role, SysUser

@main.route('/user/<username>')
def user(username):
    user = SysUser.query.filter_by(userName=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    return render_template('user.html', user=user)