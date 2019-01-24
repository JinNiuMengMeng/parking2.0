# -*- coding:utf-8 -*-
import os

debug = True
daemon = False
workers = 1
basedir = os.path.abspath(os.path.dirname(__file__))
chdir = basedir
pidfile = basedir + "/gunicorn/gunicorn.pid"
accesslog = basedir + "/gunicorn/access.log"
errorlog = basedir + "/gunicorn/error.log"
x_forwarded_for_header = 'X-FORWARDED-FOR'
bind = '0.0.0.0:8000'
worker_class = 'eventlet'
worker_connections = 2000
loglevel = 'warning'

# /home/ubuntu/Env/parkingPy27env/bin/gunicorn manage:appWeb -c gunicorn_info.py
# /home/ubuntu/Env/parkingPy27env/bin/gunicorn --chdir "/home/ubuntu/PycharmProjects/LuQiao/parking2.0" -w 1 -b 0.0.0.0:8000 manage:appWeb --worker-class eventlet --log-level debug --backlog 2000 --access-logfile "/home/ubuntu/PycharmProjects/LuQiao/parking2.0/gunicorn/access.log" --error-logfile "/home/ubuntu/PycharmProjects/LuQiao/parking2.0/gunicorn/error.log"
