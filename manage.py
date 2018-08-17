import os

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from app import create_app as app_create_app
from appWeb import create_app as appWeb_create_app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = app_create_app(os.getenv('FLASK_CONFIG') or 'default', 'app')
appWeb = appWeb_create_app(os.getenv('FLASK_CONFIG') or 'default', 'appWeb')

dm = DispatcherMiddleware(app, {
    '/appWeb': appWeb,
})


if __name__ == '__main__':
    run_simple('localhost', 8000, dm)


# manager = Manager(dm)
#
# if __name__ == '__main__':
#     manager.run()
