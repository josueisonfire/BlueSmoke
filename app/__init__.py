# Starting point for the app. If you are running locally use:
# chmod u+x run.py
#	./run.py
#
# @credits : Miguel Grinberg via https://blog.miguelgrinberg.com
# @version : 1.0.0
# @author : nuwanwre
# ==============================================================

from flask import Flask, send_from_directory
import os

app = Flask(__name__)
app.config.from_object('config')	# reference to config.py

# Route to add a favicon : Working
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, ''),
                               'favicon.ico', mimetype='image/png')

# import here to prevent circular reference at views.py
from app import views