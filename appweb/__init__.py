# coding:utf-8
import os
from flask import Flask
from config.app_config import config
from flask_socketio import SocketIO

'''
供web端访问
'''

socketio = SocketIO(async_mode="eventlet")


def create_app_2(config_name, app_name):
    tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    app = Flask(app_name, template_folder=tmpl_dir, static_folder=static_dir)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from appweb.computer_web import computer_web_main
    app.register_blueprint(computer_web_main, url_prefix="/parking2", static_url_path='/22')

    from appweb.mobile_web import mobile_web_main
    app.register_blueprint(mobile_web_main, url_prefix="/parking2/mobile")

    socketio.init_app(app)
    return app


"""
    app.url_map.default_subdomain = 'www'
    #开启SERVER_NAME和sub_domain子域名之后，static需要重新自己添加路由
    #要自己添加的static路由生效，必须开头的Flask先将static_folder=None才行，app = Flask(__name__, static_folder=None)
    app.static_url_path = "/static"
    app.static_folder = "static"
    app.add_url_rule(app.static_url_path + '/<path:filename>',
                     endpoint='static',
                     view_func=app.send_static_file,
                     subdomain="static")
    print(app.url_map)
"""


def create_app(config_name, app_name):
    tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    app = Flask(app_name, template_folder=None, static_folder=None)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.static_url_path = "/parking2/static"
    app.static_folder = static_dir
    app.template_folder = tmpl_dir

    # app.add_url_rule(app.static_url_path + '/<path:filename>',
    #                  endpoint='static',
    #                  view_func=app.send_static_file,
    #                  subdomain="static")

    from appweb.computer_web import computer_web_main
    app.register_blueprint(computer_web_main, url_prefix="/parking2")

    from appweb.mobile_web import mobile_web_main
    app.register_blueprint(mobile_web_main)

    socketio.init_app(app)
    return app
