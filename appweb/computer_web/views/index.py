# -*- coding: utf-8 -*-
from flask import render_template

from appweb.computer_web import computer_web_main


@computer_web_main.route('/')
def index():
    return render_template("computer/index.html")
