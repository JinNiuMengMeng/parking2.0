# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request
from appweb import socketio
from appweb.computer_web import computer_web_main


@computer_web_main.route('/')
def index():
    return render_template("computer/index.html")


@socketio.on('my_event', namespace='/chat')
def test_message(message):
    message["count"] = 10
    socketio.emit('my_response', message, namespace='/chat')


@computer_web_main.route('/wa')
def wahaha():
    print "------------wahaha----------"
    print request.args
    params = {x: (y[0] if isinstance(y, list) else y) for x, y in request.args.items()}
    message = {}
    message["data"] = params.get("car_type")
    message["count"] = 12
    socketio.emit('my_response', message, namespace='/chat')
    return jsonify({"result": True})


@computer_web_main.route('/dis')
def dis_stockio():
    message = {}
    message["data"] = "suc"
    socketio.emit('disconnect_request', message, namespace='/chat')
    return jsonify({"result": True})
