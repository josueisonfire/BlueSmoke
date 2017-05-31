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


# ===============================================================
#											APP CONFIGURATIONS
# ===============================================================

#app = Flask(__name__)
#app.config.from_object('config')	# load config.py


# ===============================================================
#													APP ROUTES
# ===============================================================

# Starting point
@app.route('/')
def login():
	return render_template('index.html', title = 'Please enter device ID to continue')

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
		return render_template('index.html', error = 'Sorry try again')
	
# ===============================================================
#														MAIN():
# ===============================================================
