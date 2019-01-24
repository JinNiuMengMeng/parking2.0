# -*- coding: utf-8 -*-
import os

from appweb import create_app as appweb_create_app
from appweb import socketio

appWeb = appweb_create_app(os.getenv('FLASK_CONFIG') or 'default', 'appWeb')
print appWeb.url_map
if __name__ == '__main__':
    socketio.run(appWeb, debug=True, host="0.0.0.0", port=8000)
