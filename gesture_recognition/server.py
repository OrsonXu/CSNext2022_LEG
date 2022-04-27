from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

import numpy as np
from datetime import datetime
import os
import json
from engineio.payload import Payload
Payload.max_decode_packets = 1000

port = 5000
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
count = 0


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/phone')
def phone_page():
    return render_template('phone.html')

@socketio.on('connect')
def on_connect():
    print('connected!!!')
    # emit('message', {'data': 'Connected!'})

@socketio.on('disconnect')
def on_disconnect():
    print('disconnected...')

@socketio.on('package')
def on_package(package):
    """Receive the message from the phone by head "package" and then send it out to clients by "sensor package"

    Args:
        package (str): Data from the phone
    """
    
    global count

    print(count)

    count += 1

    socketio.emit('sensor package', package)

    # socketio.emit('count',count)

@socketio.on('debug')
def on_message(info):
    print('DEBUG:', info)

if __name__ == '__main__':
    count = 0

    print("Waiting to be connected...")

    socketio.run(app, host = "0.0.0.0", port = port, debug=False)