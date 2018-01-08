[![Build Status](https://travis-ci.com/nuwanwre/BlueSmoke.svg?token=1z3xh4vnpfYyonxSVqfV&branch=master)](https://travis-ci.com/nuwanwre/BlueSmoke)

#  Cloud-Based, User-Friendly Biometric Attendance System

![BlueSmoke](/app/static/img/favicon.ico?raw=true "Optional Title")

This repository contains the source files for the system proposed in the __docs__ directory. In summary, the system provides an interface for Instructors to manage classes, attendance, generate statistical queries and manage connected devices.

If you are looking for technical details, the docs contain a detailed high level architecture of the system. We've done a comprehensive analysis on similar systems and realized many such implementations lack security/privacy measures. This system provides an additional layer of security to protect the privacy of users and their biometric data.

Hardware was designed and implemented by **@josueisonfire.**

## Repository Information

Mainly four branches.
 
* __master__   : Serves as the release branch. Major releases maybe tagged appropriatley.
* __develop__  : Development branch working on the next major release.
* __hotfixes__ : Releases that need immediate bug fixes.
* __features__ : Experimental features. Temporary branches that get deleted after merging.

## Runtime Information and Dependencies 

Backend is served via Python Flask, and uses a virtual environment for development. All packages are installed in __venv__ directory and specified in the __requirements.txt__ file.

To install dependencies, activate your virtual environment and type:
```pip install -r requirements.txt```

## Directory Structure

* BlueSmoke 
	* static 		: CSS, JS and Images go here
	* templates 	: HTML pages go here
	* __init.py__	: Load app configurations, and favicon
	* views.py 		: HTML pages, validation, and most of the rendering happens here
	* models.py		: DB information and queries go here
* flask : Configuration files. Will be loaded from OS environment on Production server

## Running Locally

To run locally : ```python run.py```

And point your browser to ``` localhost:5000```


## Deploying on your own Server

Instructions below assumes a Linux system. Tested on Ubuntu 16.04 LTS.
Before configuring Apache, make sure you have __mod_wsgi__ installed and configured for Python 2.7.

* Configure Apache2 : Edit __/etc/apache2/sites-enabled/000-default.conf__

