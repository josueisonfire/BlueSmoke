# Contains all database related configurations
# Postgre <3

from . import db
from sqlalchemy import *
import os

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
	devices = db.relationship('Devices', backref='instructor', lazy = 'dynamic')
	classes = db.relationship('Classes', backref='instructor', lazy = 'dynamic')
	
	def __repr__(self):
		return '<User {}>'.format(self.firstName)
	
# Class for Registered Devices
class Devices(db.Model):
	devId = db.Column(db.String(5), primary_key=True)
	userId = db.Column(db.Integer, db.ForeignKey('instructor.id'))
	
	def __repr__(self):
		return '<Device Id {}>'.format(self.devId)
	
# Class for Intructors and their respective classes
class Classes(db.Model):
	classId = db.Column(db.String(10), primary_key=True)
	userId = db.Column(db.Integer, db.ForeignKey('instructor.id'))
	name = db.Column(db.String(30))
	TAs = db.Column(db.String(50))
	startDate = db.Column(db.DateTime)
	endDate = db.Column(db.DateTime)
	startTime = db.Column(db.DateTime)
	endTime = db.Column(db.DateTime)

	def __repr__(self):
		return '<Class Id {}>'.format(self.classId)
	
# Dynamic table for Attendance. This table is used for Roster as 
# well. 
class Attendance:
		
	def __init__(self, name, dates):
		engine = create_engine(os.environ.get('DATABASE_URL'))
		meta = MetaData()
		attendance = Table(name, meta,
											Column('sId', String(10), primary_key=True),
											Column('firstName', String(10)),
											Column('lastName', String(20)),
											Column('fId', String(10)),
											*(Column(date, String(1)) for date in dates),
										 	mysql_engine='InnoDB')
		attendance.create(engine)
							