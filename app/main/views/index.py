# -*- coding: utf-8 -*-

from app.main import main

from flask import Flask, render_template
from flask_login import login_required, current_user


@main.route('/helloworld')
def helloworld():
    return 'hello world'



@main.route('/hello/<name>')
def hello(name="guest"):
    return render_template("hello.html", name=name)


@main.route('/index')
@main.route('/')
@login_required
def index(title="一路停车2.0"):
    return render_template("index.html", title=title)



