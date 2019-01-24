# -*- coding: utf-8 -*-

from appweb.mobile_web import mobile_web_main

from flask import render_template
from flask_login import login_required, current_user


@mobile_web_main.route('/')
@login_required
def index(title="一路停车2.0"):
    return render_template("mobile/index.html", title=title)
