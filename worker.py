'''

	This app defines the worker process to communicate with the 
	device. It will be running continually in the background.
	
	$PORT to be specified
	
	
	@author 	: 	nuwanwre via blueSmoke. C412
	@version 	: 	1.0.0
	
	CRITICAL : ** IMPLEMENT THREADS **
	
'''

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app)


@app.route('/')
def index():
	return render_template('socketIndex.html')
	
@socketio.on('my event', namespace='/test')
def test_message(message):
	emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
	emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
	emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected')


if __name__ == '__main__':
	port = int(os.environ.get("PORT_CONNECT", 5001))
	socketio.run(app, debug = True, hodt = '0.0.0.0', port  = port)