# Starting point for the app. If you are running locally use:
# chmod u+x run.py
#	./run.py
#
# @credits : Miguel Grinberg via https://blog.miguelgrinberg.com
# @version : 1.0.0
# @author : nuwanwre via BlueSmoke Labs C412.
# ==============================================================

from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

app = Flask(__name__)
# reference to config.py
app.config.from_object(Config)	
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#from models import dbObject

# Route to add a favicon : Working
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, ''),
                               'favicon.ico', mimetype='image/png')

# import here to prevent circular reference at views.py
from . import views, models