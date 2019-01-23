# -*- coding: utf-8 -*-
from flask import render_template

from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import biz_logging


@computer_web_main.route('/')
@biz_logging
def index():
    return render_template("computer/index.html")
