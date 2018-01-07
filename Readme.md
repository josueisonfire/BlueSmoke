[![Build Status](https://travis-ci.com/nuwanwre/BlueSmoke.svg?token=1z3xh4vnpfYyonxSVqfV&branch=master)](https://travis-ci.com/nuwanwre/BlueSmoke)

#  Cloud-Based, User-Friendly Biometric Attendance System

![BlueSmoke](/app/static/img/favicon.ico?raw=true "Optional Title")

This repository contains the Web Interface for gathering attendance data, and managing all connected devices. 

## Repository Information

Mainly four branches.
	* __master__  : Serves as the release branch. Major releases maybe tagged appropriatley.
	* __develop__ : Develpoment branch working on the next major release.
	* __hotfixes__: Releases that need immedaite bug fixing.
	* __features__: Experimental features. Temporary branches.

## Runtime Information

Backend is served via Python Flask, and uses a virtual environment for development. All packages are installed in __venv__ directory.

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



