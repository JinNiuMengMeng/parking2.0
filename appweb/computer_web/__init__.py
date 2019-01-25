# -*- coding:utf-8 -*-
import os
from flask import Blueprint


'''
供电脑 web 端访问
'''

computer_web_main = Blueprint(
    name='computer_web_main',
    import_name=__name__,
    template_folder=os.getcwd() + "/appweb/templates",
    static_folder=os.getcwd() + "/appweb/static"
)

from appweb.computer_web.views import index, error_handler, user_view
