[![Build Status](https://travis-ci.com/nuwanwre/BlueSmoke.svg?token=1z3xh4vnpfYyonxSVqfV&branch=master)](https://travis-ci.com/nuwanwre/BlueSmoke)

# BlueSmoke Labs - Cloud-Based, User-Friendly Biometric Attendance System

![BlueSmoke](/app/static/img/favicon.ico?raw=true "Optional Title")

This repository conatins all the sirue files for the system. Python requirements for the app to function are included in the **requirements.txt** file. 


## Directory Structure

* app 
	* static : CSS, JS and Images go here
	* templates : HTML pages go here
	* __init.py__ : Load app configurations, and favicon
	* views.py : HTML pages, validation, and most of the renedering happens here
* flask 
* Procfile : Configurations for Heroku 	Deployment
* requirements.py : Required Python runtimes to be installed at Heroku 
* run.py : App starts here

## Running the app

To run locally :

```
python run.py
```

And point your browser to ``` localhost:5000```



