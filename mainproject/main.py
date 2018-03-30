from flask import Flask
from flask import render_template, request, flash, redirect, session, abort, url_for
import MySQLdb
import os
from collections import OrderedDict

db = MySQLdb.connect("localhost","root","shrey1234","FosslipyDB")


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("homebody.html")


@app.route('/adminhome',methods = ['POST', 'GET'])
def adminhome():

	if request.form['psw'] == 'admin2018' and request.form['email'] == 'admin@2018.com':
		session['logged_in'] = True
		result = request.form
		return render_template("adminbody.html",result = result)

	else:

		Username = request.form['email'] 
		Password = request.form['psw']
		session['logged_in']= True

		cursor = db.cursor()
		cursor.execute("select * from Registration where Username ='"+Username+"' and Password ='"+Password+"'")
		user = cursor.fetchall()

		if len(user) is 1:
			return render_template('userbody.html')
		else:
			msg = ("Invalid email or password!")
			msg1 = ("Please Login with Correct Email/Password!")
			return render_template('Login.html',msg=msg, msg1=msg1)




@app.route("/userbody")
def userbody():

	return render_template("userbody.html")
	#return redirect(url_for("adminhome"))


@app.route('/userhome',methods =['POST', 'GET'])
def userhome():
	if request.method =='POST':
		Name = request.form['name']
		Username = request.form['email']
		Password = request.form['psw']

		cursor = db.cursor()
		cursor.execute("""
	INSERT INTO Registration(Name,Username,Password) 
	VALUES (%s,%s,%s) """, (Name,Username,Password))
		db.commit()

	msg = ("Registration successfull!")
	return render_template("Login.html",msg=msg)


@app.route('/adminmain')
def adminmain():
	return render_template("adminbody.html")



@app.route('/freeform2')
def freeform2():
    #data1=OrderedDict([('College_Name',['','text']), ('Location',['','text']), ('HOD_Name',['','text']), ('Contact_Details',['','tel']), ('Seminar_Date',['','Date']), ('Topic',['','text']), ('Expectation',['','textarea'])])
    return render_template("freeform.html")

@app.route('/upcomingform')
def upcomingform():
    data1=OrderedDict([('College_Name',['','text']), ('Location',['','text']), ('HOD_Name',['','text']), ('Contact_Details',['','tel']), ('Seminar_Date',['','Date']), ('Topic',['','text']),('Approach_Date',['','Date']), ('Follow_Up1',['','textarea']),('Follow_Up2',['','textarea']),('Follow_Up3',['','textarea'])])
    return render_template("updateform.html",data=data1,frmtype="Update")

@app.route('/upcomingeditform')
def upcomingeditform():
    data1=OrderedDict([('College_Name',['','text']), ('Location',['','text']), ('HOD_Name',['','text']), ('Contact_Details',['','tel']), ('Seminar_Date',['','Date']), ('Topic',['','text']),('Approach_Date',['','Date']), ('Follow_Up1',['','textarea']),('Follow_Up2',['','textarea']),('Follow_Up3',['','textarea'])])
    return render_template("updateform.html",data=data1,frmtype="Update1")


@app.route('/paidform')
def paidform():
    data1=OrderedDict([('College_Name',['','text']), ('Location',['','text']), ('HOD_Name',['','text']), ('Contact_Details',['','tel']), ('Seminar_Date',['','Date']), ('Topic',['','text']),('Remark',['','textarea'])])
    return render_template("paidform.html",data=data1,frmtype="Update2")


@app.route('/Enter', methods = ['POST', 'GET'])
def Enter():

	if request.method=='POST':
		College_Name = request.form['Colname']
		Location = request.form['loc']
		HOD_Name = request.form['hod']
		Contact_Details = request.form['con']
		Seminar_Date = request.form['date']
		Topic = request.form['top']
		Expectation = request.form['expect']
	
		cursor = db.cursor()
		cursor.execute("""
	INSERT INTO Free_Workshop(College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation) 
	VALUES (%s,%s,%s,%s,%s,%s,%s) """, (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation))
		db.commit()

	cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
	return render_template("freeworkshoptable.html",data = data)
	
	db.close()

		

#Free Workshop functions
@app.route('/result', methods = ['POST', 'GET'])
def result():

	'''if request.method=='POST' and request.form['submit'] == "Enter":
		College_Name = request.form['Colname']
		Location = request.form['loc']
		HOD_Name = request.form['hod']
		Contact_Details = request.form['con']
		Seminar_Date = request.form['date']
		Topic = request.form['top']
		Expectation = request.form['expect']
	
		cursor = db.cursor()
		cursor.execute("""
	INSERT INTO Free_Workshop(College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation) 
	VALUES (%s,%s,%s,%s,%s,%s,%s) """, (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation))
		db.commit()'''
		#msg = "Record successfully added"
		#return render_template("freeworkshoptable.html",msg = msg)

	if request.method=='POST' and request.form['submit'] == "Edit":
		College_Name = request.form['College_Name']
        Location = request.form['Location']
        HOD_Name = request.form['HOD_Name']
        Contact_Details = request.form['Contact_Details']
        Seminar_Date = request.form['Seminar_Date']
        Topic = request.form['Topic']
        Expectation = request.form['Expectation']
        id1=request.form['id1']
        cursor = db.cursor()
        cursor.execute ("""
            UPDATE Free_Workshop 
            SET College_Name=%s, Location=%s, HOD_Name=%s, Contact_Details=%s, Seminar_Date=%s, Topic=%s, Expectation=%s 
            WHERE F_id=%s""", (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Expectation,id1))
        print("record edited")
        db.commit()


	cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
	return render_template("freeworkshoptable.html",data = data)
	
	db.close()

@app.route('/edit',methods = ['POST','GET'])
def edit():
    cursor = db.cursor()
    query = "select * from Free_Workshop where F_id=" + request.args['id']
    
    data=cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        data1=OrderedDict([('id1',[i[0],'hidden']), ('College_Name',[i[1],'text']), ('Location',[i[2],'text']), ('HOD_Name',[i[3],'text']), ('Contact_Details',[i[4],'tel']), ('Seminar_Date',[i[5],'Date']), ('Topic',[i[6],'text']), ('Expectation',[i[7],'textarea'])])
    return render_template("EditForm.html",data=data1,frmtype="Edit")

@app.route('/upedit',methods = ['POST','GET'])
def upedit():
    cursor = db.cursor()
    query = "select U_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3 from Upcoming_Workshop where U_id=" + request.args['id']
    
    data=cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        data1=OrderedDict([('id1',[i[0],'hidden']), ('College_Name',[i[1],'text']), ('Location',[i[2],'text']), ('HOD_Name',[i[3],'text']), ('Contact_Details',[i[4],'tel']), ('Seminar_Date',[i[5],'Date']), ('Topic',[i[6],'text']), ('Approach_Date',[i[7],'Date']), ('Follow_Up1',[i[8],'textarea']),('Follow_Up2',[i[9],'textarea']),('Follow_Up3',[i[10],'textarea'])])
    return render_template("upedit.html",data=data1,frmtype="Update1")


@app.route('/paidedit',methods = ['POST','GET'])
def paidedit():
    cursor = db.cursor()
    query = "select P_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark from Paid_Workshop where P_id=" + request.args['id']
    
    data=cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        data1=OrderedDict([('id1',[i[0],'hidden']), ('College_Name',[i[1],'text']), ('Location',[i[2],'text']), ('HOD_Name',[i[3],'text']), ('Contact_Details',[i[4],'tel']), ('Seminar_Date',[i[5],'Date']), ('Topic',[i[6],'text']), ('Remark',[i[7],'textarea'])])
    return render_template("paidupdate.html",data=data1,frmtype="Update3")


@app.route('/delete',methods = ['POST','GET'])
def delete():
	cursor =db.cursor()
	cursor.execute("delete from Free_Workshop where F_id=" + request.args['id'])
	db.commit()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
	return render_template("freeworkshoptable.html",data=data)
	db.close()

@app.route('/delete1',methods = ['POST','GET'])
def delete1():
	cursor =db.cursor()
	cursor.execute("delete from Upcoming_Workshop where U_id=" + request.args['id'])
	db.commit()
	cursor.execute("select U_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3 from Upcoming_Workshop")
	data=cursor.fetchall()
	return render_template("upcomingworkshoptable.html",data=data)
	db.close()

@app.route('/delete2',methods = ['POST','GET'])
def delete2():
	cursor =db.cursor()
	cursor.execute("delete from Paid_Workshop where P_id=" + request.args['id'])
	db.commit()
	cursor.execute("select P_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark from Paid_Workshop")
	data=cursor.fetchall()
	return render_template("paidworkshoptable.html",data=data)
	db.close()


@app.route('/update',methods = ['POST','GET'])
def update():
    cursor = db.cursor()
    query = "select * from Free_Workshop where F_id=" + request.args['id']
    
    data=cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        data1=OrderedDict([('id1',[i[0],'hidden']), ('College_Name',[i[1],'text']), ('Location',[i[2],'text']), ('HOD_Name',[i[3],'text']), ('Contact_Details',[i[4],'tel']), ('Seminar_Date',[i[5],'Date']), ('Topic',[i[6],'text']),('Approach_Date',[i[7],'Date']), ('Follow_Up1',['','textarea']),('Follow_Up2',['','textarea']),('Follow_Up3',['','textarea'])])
    return render_template("updateform.html",data=data1,frmtype="Update")


@app.route('/updateup',methods = ['POST','GET'])
def updateup():
    cursor = db.cursor()
    query = "select U_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic from Upcoming_Workshop where U_id=" + request.args['id']
    #query = "select * from Upcoming_Workshop where F_id=" + request.args['id']
    data=cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        data1=OrderedDict([('id1',[i[0],'hidden']), ('College_Name',[i[1],'text']), ('Location',[i[2],'text']), ('HOD_Name',[i[3],'text']), ('Contact_Details',[i[4],'tel']), ('Seminar_Date',[i[5],'Date']), ('Topic',[i[6],'text']),('Remark',['','textarea'])])
    return render_template("paidform.html",data=data1,frmtype="Update2")

@app.route('/result1', methods = ['POST', 'GET'])
def result1():
   
    if request.method=='POST' and request.form['submit']=="Update":
		College_Name = request.form['College_Name']
		Location = request.form['Location']
		HOD_Name = request.form['HOD_Name']
		Contact_Details = request.form['Contact_Details']
		Seminar_Date = request.form['Seminar_Date']
		Topic = request.form['Topic']
		Approach_Date = request.form['Approach_Date']
		Follow_Up1 = request.form['Follow_Up1']
		Follow_Up2 = request.form['Follow_Up2']
		Follow_Up3 = request.form['Follow_Up3']
		#id1=request.form['id1']
	
		cursor = db.cursor()
		cursor.execute("""
	INSERT INTO Upcoming_Workshop(College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3) 
	VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """, (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3))
		db.commit()
		
	

    if request.method=='POST' and request.form['submit'] == "Update1":
		College_Name = request.form['College_Name']
		Location = request.form['Location']
		HOD_Name = request.form['HOD_Name']
		Contact_Details = request.form['Contact_Details']
		Seminar_Date = request.form['Seminar_Date']
		Topic = request.form['Topic']
		Approach_Date = request.form['Approach_Date']
		Follow_Up1 = request.form['Follow_Up1']
		Follow_Up2 = request.form['Follow_Up2']
		Follow_Up3 = request.form['Follow_Up3']
		id1=request.form['id1']
		cursor = db.cursor()
		cursor.execute ("""
            UPDATE Upcoming_Workshop 
            SET College_Name=%s, Location=%s, HOD_Name=%s, Contact_Details=%s, Seminar_Date=%s, Topic=%s, Approach_Date=%s, Follow_Up1=%s,Follow_Up2=%s,Follow_Up3=%s 
            WHERE U_id=%s""", (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3,id1))
		print("record edited")
		db.commit()


    cursor = db.cursor()
    cursor.execute("select U_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3 from Upcoming_Workshop")
    data=cursor.fetchall()
    return render_template("upcomingworkshoptable.html",data=data)
    db.close()


@app.route('/result2', methods = ['POST', 'GET'])
def result2():
   
    if request.method=='POST' and request.form['submit']=="Update2":
		College_Name = request.form['College_Name']
		Location = request.form['Location']
		HOD_Name = request.form['HOD_Name']
		Contact_Details = request.form['Contact_Details']
		Seminar_Date = request.form['Seminar_Date']
		Topic = request.form['Topic']
		Remark = request.form['Remark']
		#id1=request.form['id1']
	
		cursor = db.cursor()
		cursor.execute("""
	INSERT INTO Paid_Workshop(College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark) 
	VALUES (%s,%s,%s,%s,%s,%s,%s) """, (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark))
		db.commit()

    if request.method=='POST' and request.form['submit'] == "Update3":
		College_Name = request.form['College_Name']
		Location = request.form['Location']
		HOD_Name = request.form['HOD_Name']
		Contact_Details = request.form['Contact_Details']
		Seminar_Date = request.form['Seminar_Date']
		Topic = request.form['Topic']
		Remark = request.form['Remark']
		id1=request.form['id1']
		cursor = db.cursor()
		cursor.execute ("""
            UPDATE Paid_Workshop 
            SET College_Name=%s, Location=%s, HOD_Name=%s, Contact_Details=%s, Seminar_Date=%s, Topic=%s, Remark=%s 
            WHERE P_id=%s""", (College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark,id1))
		print("record edited")
		db.commit()

    cursor = db.cursor()
    cursor.execute("select P_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark from Paid_Workshop")
    data=cursor.fetchall()
    return render_template("paidworkshoptable.html",data=data)
    db.close()


	


@app.route('/freeworkshoptable')
def freeworkshoptable():
	cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
    	return render_template("freeworkshoptable.html",data= data)
	db.close()

@app.route('/userfreetable')
def userfreetable():
	cursor = db.cursor()
	cursor.execute("select * from Free_Workshop")
	data=cursor.fetchall()
    	return render_template("userfreetable.html",data= data)
	db.close()


@app.route('/upcomingworkshoptable')
def upcomingworkshoptable():
	cursor = db.cursor()
	#cursor.execute("select * from Upcoming_Workshop")
	cursor.execute("select U_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3 from Upcoming_Workshop")
	data=cursor.fetchall()
    	return render_template("upcomingworkshoptable.html",data= data)
	db.close()

@app.route('/useruptable')
def useruptable():
	cursor = db.cursor()
	#cursor.execute("select * from Upcoming_Workshop")
	cursor.execute("select U_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Approach_Date,Follow_Up1,Follow_Up2,Follow_Up3 from Upcoming_Workshop")
	data=cursor.fetchall()
    	return render_template("useruptable.html",data= data)
	db.close()


@app.route('/paidworkshoptable')
def paidworkshoptable():
	cursor = db.cursor()
	#cursor.execute("select * from Upcoming_Workshop")
	cursor.execute("select P_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark from Paid_Workshop")
	data=cursor.fetchall()
    	return render_template("paidworkshoptable.html",data= data)
	db.close()

@app.route('/userpaidtable')
def userpaidtable():
	cursor = db.cursor()
	#cursor.execute("select * from Upcoming_Workshop")
	cursor.execute("select P_id,College_Name,Location,HOD_Name,Contact_Details,Seminar_Date,Topic,Remark from Paid_Workshop")
	data=cursor.fetchall()
    	return render_template("userpaidtable.html",data= data)
	db.close()
    




if (__name__ == "__main__"):
	app.secret_key = os.urandom(12)
	app.run(debug=True)
