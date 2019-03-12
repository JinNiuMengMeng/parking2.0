# coding:utf-8

from flask import Flask
from config.app_config import config
from flask_socketio import SocketIO

socketio = SocketIO(async_mode="eventlet")


def create_app(config_name, app_name):

    app = Flask(app_name, template_folder=None, static_folder=None)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from appweb.computer_web import computer_web_main
    app.register_blueprint(computer_web_main, url_prefix="/parking2")

    from appweb.mobile_web import mobile_web_main
    app.register_blueprint(mobile_web_main, url_prefix="/parking2/mobile")
    socketio.init_app(app)

    return app
