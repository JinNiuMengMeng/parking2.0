from flask import render_template
from appweb.mobile_web import mobile_web_main

"""
@mobile_web_main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@mobile_web_main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
"""