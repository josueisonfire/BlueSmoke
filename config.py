# This file contains the necessary configuration to run the app
#
#	Python Flask <3
#
# @credits : Miguel Grinberg via https://blog.miguelgrinberg.com
# @version : 1.0.0
# @author : nuwanwre via BlueSmoke Labs. C412
# ===============================================================

# No use of seperate classes. Will be added later
import os

WTF_CSRF_ENABLED = True			# Prevent Cross-Site request forgery
SECRET_KEY = 'bluesmoke'


# !!! IMPORTANT !!!
# For local deployment only
SQLALCHEMY_DATABASE_URI = "postgresql://nuwanwre:bluesmoke@localhost/blueSmoke"
# Modification tracking disabled to use less memory
SQLALCHEMY_TRACK_MODIFICATIONS = False


