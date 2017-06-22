'''

	This app defines the worker process to communicate with the 
	device. It will be running continually in the background.
	
	$PORT to be specified
	
	
	@author 	: 	nuwanwre via blueSmoke. C412
	@version 	: 	1.0.0
	
'''

import os
import logging
# import redis
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets

# REDIS_URL = os.environ['REDIS_URL']
# REDIS_CHAN = 'device'


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/listen')
def listen(ws):
	# Recieve incoming traffic
	while not ws.closed:
		# gevent.sleep(0.1)
		message = ws.receive()
		
		if message:
			app.logger.info(u'Inserting message  : {}'.format(message))
		

if __name__ == '__main__':
	app.run(debug = True, port = 1010)