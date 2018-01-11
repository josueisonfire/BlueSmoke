# Contains all database related configurations
# Postgre <3

from . import db
# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy.orm import mapper
# from db import metadata, db_session

# Class relations holds all the class related data
# Tuples and their types :
# 	ID : varchar(10)
#		Name : varchar(30)
#		TAs : varchar(50)
#		startDate : date
#		endDate : date
#		startTime : time without timezone
#	 	endTime : time without timezone 
# 	attendanceTable : varchar(10)

# Class for Instructor relation 
class Instructor(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(10))
	lastName = db.Column(db.String(20))
	password = db.Column(db.String(128))
	
	def __repr__(self):
		return '<User {}>'.format(self.firstName)
	
# Class for Registered Devices
