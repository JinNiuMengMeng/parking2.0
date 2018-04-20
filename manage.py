import os
from app import create_app, db

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
