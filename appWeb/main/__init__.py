from flask import Blueprint

appWeb_main = Blueprint('appWeb_main', __name__)

from appWeb.main.views import index, error_handler, user_view
