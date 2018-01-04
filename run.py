# Starting point for the app. If you are running locally use:
# chmod u+x run.py
#	./run.py
#
# Python Flask <3
#
# @credits : Miguel Grinberg via https://blog.miguelgrinberg.com
# @version : 1.0.0
# @author : nuwanwre via BlueSmoke Labs. C412
# ===============================================================


#!flask/bin/python
from app import app
#from worker import worker

# Encapsulate Run
#
# Notes: Running on Heroku will attach custom ports, so listening 
# on a certain port will tricky.
#
# Workaround: worker process will run on a different domain
if __name__ == '__main__':
	#port = int(os.environ.get("PORT_MAIN", 5000))
	app.run(host='0.0.0.0', port=5000, debug = True)
