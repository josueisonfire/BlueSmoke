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
from worker import worker

# Encapsulate Run
if __name__ = '__main__':
	port = int(os.environ.get("PORT", 5001))
	app.run(debug = True, host = "0.0.0.0", port = port)