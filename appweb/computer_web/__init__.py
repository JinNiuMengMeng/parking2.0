import os

from flask import Blueprint

computer_web_main = Blueprint('computer_web_main', import_name=__name__, template_folder=os.getcwd() + "/appweb/templates", static_folder=os.getcwd() + "/appweb/static")

from appweb.computer_web.views import index, error_handler, user_view

print os.getcwd()