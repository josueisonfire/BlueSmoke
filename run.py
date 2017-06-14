# Starting point for the app. If you are running locally use:
# chmod u+x run.py
#	./run.py
#
# @credits : Miguel Grinberg via https://blog.miguelgrinberg.com
# @version : 1.0.0
# @author : nuwanwre
# ===============================================================


#!flask/bin/python
from app import app

# Encapsulate Run
if __name__ = '__main__':
	app.run(debug = True)