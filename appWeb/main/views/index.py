# -*- coding: utf-8 -*-

from appWeb.main import appWeb_main
from appWeb.plugins.decorators import biz_logging


@appWeb_main.route('/hello')
def helloworld():
    return 'appWeb<br>hello world'


@appWeb_main.route('/hello/<name>')
def hello(name="guest"):
    return 'appWeb<br>hello %s' % name


@appWeb_main.route('/index')
@appWeb_main.route('/')
@biz_logging
def index(title="一路停车2.0"):
    return "appWeb<br>这是首页"
