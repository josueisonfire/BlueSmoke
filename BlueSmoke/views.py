# This file defines the starting point for the Web App.
# All the imports here should be included in the requirements.txt
# to pass the build. 
# 
#	@version 	: 1.0.0
# @author 	:	nuwanwre

# ===============================================================
#													IMPORTS
# ===============================================================
from . import app
from flask import Flask, render_template, redirect, request, session, jsonify, url_for
import os
from werkzeug import generate_password_hash, check_password_hash

# ==============================================================
#											ENVIRONMENT VARIABLES
#
# 	Change this variables as you wish. However some setings may
#			make the web app vulnerable to security exploits.
# ==============================================================


# ===============================================================
#											APP CONFIGURATIONS
# ===============================================================


# ===============================================================
#													APP ROUTES
# ===============================================================

# >> Starting point
@app.route('/')
def login():
	return render_template('index.html', title = 'Please enter device ID to continue')

# >> Route to validate a device
@app.route('/validateDevice', methods = ['POST', 'GET'])
def validateDevice():
	try:
		deviceID = request.form['deviceID']
		
		# Bypass
		if (deviceID == "demo"):
			session['user'] = deviceID
			
	except Exception as e:
		return e
		
	if(session['user'] == deviceID):
		return "Validated"
	else:
		return render_template('index.html', error = 'Sorry try again')
	
# >> Route to display main page
@app.route('/home')
def home():
	try:
		return render_template('home.html')
	except Exception as e:
		return str(e)
	
# >> Route to display base html
@app.route('/base', methods = ['GET'])
def base():
	try:
		print getStudents()
		return render_template('base.html', title = "Base", students = getStudents())
	except Exception as e:
		return str(e)
	
# >> Route to generate the tab
@app.route('/getTab', methods = ['GET'])
def getTab():
	try:
		index = int(request.args.get('Tab'))
		if (index == 0):
			return render_template('roster.html')
		elif (index == 1):
			return render_template('attendance.html')
		elif (index == 2):
			return render_template('statistics.html')
		else: 
			return str(index)
		
	except Exception as e:
		return str(e)
	
# >> Route to accept incoming connections
@app.route('/bluesmoke', methods=['POST'])
def my_test_endpoint():
	input_json = request.get_json(force=True) 
	
	# force=True, above, is necessary if another developer 
	# forgot to set the MIME type to 'application/json'
	
	# Register fingerprint
	if (input_json['method'] == "Register"):
		registerFID(input_json['sid'], input_json['fid'])
		# print 'data from client:', input_json['method']
		dictToReturn = {'Response':'Success'}
		return jsonify(dictToReturn)
	else:
		registerAttendance(input_json['fid'])
		# print 'data from client:', input_json['method']
		dictToReturn = {'Response':'Success'}
		return jsonify(dictToReturn)
	
	

# >> Route to add New Student
@app.route('/addNewStudent', methods=['POST', 'GET'])
def addStudent():
	try:
		fn = request.form['fn'] # first name
		ln = request.form['ln'] # last name
		sid = request.form['sid'] # student id
		fid = request.form['fid'] # fingerprint id
		
		addNewStudentData(fn, ln, sid, fid)
		addNewAttendance(sid, fn, ln)
		return redirect(url_for('base'))
	except Exception as e:
		return e
	
# >> Route to get student data
@app.route('/getStudentData')
def getStudentData():
	return jsonify(getStudents())

# >> Route to get attendance data
@app.route('/getAttendanceData')
def getAttendanceData():
	return jsonify(getAttendance())

# >> Route to test db connections
@app.route('/tests/db')
def test_db():
	try:
		
		return "Success"
	except Exception as e:
		return e
	
# >> Route to send csv data to plot
@app.route('/stats')
def getStats():
	return str(getCSVData())
	
		
	
	
	
# ===============================================================
#														MAIN():
# ===============================================================


# ===============================================================
#														HELPERS AND PLASTERS
# ===============================================================

def addNewStudentData(fn, ln, sid, fid):
	try:
		query = "INSERT INTO Student(FirstName, LastName, sID, fID) VALUES (%s, %s, %s, %s)"
		args = (fn, ln, sid, fid)
		cursor.execute(query, args)
		data = cursor.fetchall()

		if len(data) is 0:
			conn.commit()

		else:
			return "Insertion Error at Roster"
		
	except Exception as e:
		return e

def addNewAttendance(sid, fn, ln):
	try:
		# Add to Attendance Table
		print "Adding to attendance"

		query = "INSERT INTO Attendance(sID, FirstName, LastName, Day1, Day2, Day3, Day4, Day5, Day6, Day7) VALUES (%s, %s, %s, '-', '-', '-', '-', '-', '-', '-')"
		args = (sid, fn, ln)
		cursor.execute(query, args)
		data = cursor.fetchall()


		if len(data) is 0:
			conn.commit()

		else:
			return "Insertion Error at Attendance"
		
	except Exception as e:
		print e
		return e

def getStudents():
	try:
		query = "SELECT * FROM Student"
		cursor.execute(query)
		data = cursor.fetchall()
		tmp = []
		if(len(data) > 0):
			for row in data:
				tmp.append({'FirstName':row[0],
									  'LastName':row[1],
										'sID':row[2],
										'fID':row[3]
									 })
			return tmp
		else:
			return []
	except Exception as e:
		return "Error at getStudent():" + str(e)

def getAttendance():
	try:
		query = "SELECT * FROM Attendance"
		cursor.execute(query)
		data = cursor.fetchall()
		tmp = []
		if(len(data) > 0):
			for row in data:
				tmp.append({'sID':row[0],
									  'FirstName':row[1],
										'LastName':row[2],
										'Day1':row[3],
										'Day2':row[4],
										'Day3':row[5],
										'Day4':row[6],
										'Day5':row[7],
										'Day6':row[8],
										'Day7':row[9]
									 })
			return tmp
		else:
			return []
		
	except Exception as e:
		print e
		return e

	
# Update fid after initial fingerprint registration	
def registerFID(sid, fid):
	try:
		query = "UPDATE Student SET fID = %s WHERE sID = %s"
		args = (fid, sid)

		cursor.execute(query, args)
		data = cursor.fetchall()
		if len(data) is 0:
			conn.commit()

		else:
			return "Update Error at Student"
	
	except Exception as e:
		print e
		return e
	
# Update Attendance on table
def registerAttendance(fid):
	try:
		query = "SELECT sID FROM Student WHERE fID = %s"
		args = (fid)
		
		cursor.execute(query, args)
		data = cursor.fetchall()
		
		if (len(data) > 0):
			query = "UPDATE Attendance SET Day7='O' WHERE sID = %s"
			args = (data[0])
			
			cursor.execute(query, args)
			data = cursor.fetchall()
			if len(data) is 0:
				conn.commit()

			else:
				return "Update Error at Attendance"

		else:
			return "Select Error at Student"
		
	except Exception as e:
		print e
		return e	
	
def getCSVData():
	try:
		query = "select  sum(case when Day1='O' then 1 else 0 end) as Day1, sum(case when Day2='O' then 1 else 0 end) as Day2, sum(case when Day3='O' then 1 else 0 end) as Day3, sum(case when Day4='O' then 1 else 0 end) as Day4, sum(case when Day5='O' then 1 else 0 end) as Day5, sum(case when Day6='O' then 1 else 0 end) as Day6, sum(case when Day7='O' then 1 else 0 end) as Day7 from Attendance"
		
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) > 0):
			tmp = ""
			for row in data:
				for i in range(0,7):
					tmp += str(i+1) + '-Dec-17' + ',' + str(row[i]) + '\n'
			header = 'day,count\n'
			
			return header + tmp
		
		else:
			print "No data on CSV"
	
	except Exception as e:
		print e
		return e