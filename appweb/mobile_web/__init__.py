import os

from flask import Blueprint

mobile_web_main = Blueprint('mobile_web_main', import_name=__name__, template_folder=os.getcwd() + "/appweb/templates", static_folder=os.getcwd() + "/appweb/static")
from appweb.mobile_web.views import index, error_handler, user_view
