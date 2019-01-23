# -*- coding:utf-8 -*-
import os

debug = True
daemon = False
workers = 1
basedir = os.path.abspath(os.path.dirname(__file__))
pidfile = basedir + "/gunicorn/gunicorn.pid"
accesslog = basedir + "/gunicorn/log/access.log"
errorlog = basedir + "/gunicorn/log/error.log"
x_forwarded_for_header = 'X-FORWARDED-FOR'
bind = '0.0.0.0:8000'
worker_class = 'eventlet'
worker_connections = 2000
loglevel = 'warning'

# /home/ubuntu/Env/parkingPy27env/bin/gunicorn manage:appWeb -c gunicorn_info.py
