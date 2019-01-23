import os

from flask import Blueprint

mobile_web_main = Blueprint('mobile_web_main', import_name=__name__)
from appweb.mobile_web.views import index, error_handler, user_view
