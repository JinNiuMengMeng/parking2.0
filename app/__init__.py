# coding:utf-8
import os
import jinja2
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config.app_config import config

'''
供手机端app访问
'''

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name, app_name):
    app = Flask(app_name)

    tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    app.jinja_loader = jinja2.FileSystemLoader(tmpl_dir)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
