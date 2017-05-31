# This file defines the starting point for the Web App.
# All the imports here should be included in the requirements.txt
# to pass the build. 
# 
#	@version 	: 1.0.0
# @author 	:	nuwanwre

# ===============================================================
#													IMPORTS
# ===============================================================
from app import app
from flask import Flask, render_template, redirect, request, session, send_from_directory
# import MySQLdb
import os
from werkzeug import generate_password_hash, check_password_hash

# ==============================================================
#											ENVIRONMENT VARIABLES
#
# 	Change this variables as you wish. However some setings may
#			make the web app vulnerable to security exploits.
# ==============================================================


SECRET_KEY = 'bluesmoke'
# ===============================================================
#											APP CONFIGURATIONS
# ===============================================================

#app = Flask(__name__)
#app.config.from_object('config')	# load config.py
app.secret_key = SECRET_KEY


# ===============================================================
#													APP ROUTES
# ===============================================================

# Starting point
@app.route('/')
def login():
	return render_template('index.html')


# Route to add a favicon : Not working
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, ''),
                               'favicon.ico', mimetype='image/png')

# Route to validate a device
@app.route('/validateDevice', methods = ['POST', 'GET'])
def validateDevice():
	try:
		deviceID = request.form['deviceID']
		
		# Bypass
		if (deviceID == "demo"):
			session['user'] = deviceID
			
	except Exception as e:
		return e
		
	if(session['user'] == deviceID):
		return "Validated"
	else:
		return "Device validation failed"
	
# ===============================================================
#														MAIN():
# ===============================================================
