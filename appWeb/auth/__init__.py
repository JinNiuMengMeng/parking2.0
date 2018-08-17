from flask import Blueprint

appWeb_auth = Blueprint('appWeb_auth', __name__)

from appWeb.auth.views import views


