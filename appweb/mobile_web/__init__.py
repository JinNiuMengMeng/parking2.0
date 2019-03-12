# -*- coding:utf-8 -*-
import os
from flask import Blueprint

"""
手机网页端
"""

mobile_web_main = Blueprint(
    name='mobile_web_main',
    import_name=__name__,
    template_folder=os.getcwd() + "/appweb/templates",
    static_folder=os.getcwd() + "/appweb/static"
)

from appweb.mobile_web.views import index, error_handler, user_view
