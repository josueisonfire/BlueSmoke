# This file defines the starting point for the Web App.
# All the imports here should be included in the requirements.txt
# to pass the build. 
# 
#	@version 	: 1.0.0
# @author 	:	nuwanwre

# ===============================================================
#													IMPORTS
# ===============================================================

from flask import Flask, render_template, redirect
# import MySQLdb
from werkzeug import generate_password_hash, check_password_hash


# ===============================================================
#											APP CONFIGURATIONS
# ===============================================================

app = Flask(__name__)



# ===============================================================
#													APP ROUTES
# ===============================================================

@app.route('/')
def login():
	return render_template('index.html')
	
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, ''),
                               'favicon.ico', mimetype='image/png')
	
	
# ===============================================================
#														MAIN():
# ===============================================================

if __name__ == '__main__':
    app.run(debug=True, port = 5002)
