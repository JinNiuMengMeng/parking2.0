from flask import Blueprint

computer_web_main = Blueprint('computer_web_main', import_name=__name__)

from appweb.computer_web.views import index, error_handler, user_view
