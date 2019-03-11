# -*- coding: utf-8 -*-
from flask import render_template, request
from appweb import socketio
from appweb.computer_web import computer_web_main
from appweb.plugins.decorators import get_result


@computer_web_main.route('/')
def index():
    return render_template("computer/index.html")


@computer_web_main.route('/recvLaneMsg')
def recv_lane_mesg():
    params = {x: (y[0] if isinstance(y, list) else y) for x, y in request.args.items()}
    message = {
        "data": params.get("car_type"),
        "count": 12,
    }
    socketio.emit('my_response', message)
    return get_result()


@socketio.on('my_event')
def socket_io_login(message):
    socketio.emit('my_response', message)


@socketio.on('disconnect')
def socket_io_logout():
    pass
