# Contains all database related configurations
# Postgre <3

# from app import db
# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy.orm import mapper
# from db import metadata, db_session
import psycopg2


try:
	self.conn = psqycopg2.connect("dbname='blueSmoke' user='nuwanwre' host='localhost' password='bluesmoke'")
	self.cur = self.conn.cursor()
except Exception as e:
	return e
		

try:
	self.cur.execute("""SELECT * from Classes""")
	return self.cur.fetchall()
except Exception as e:
	return e
		
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