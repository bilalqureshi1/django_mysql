from __future__ import print_function
import pymysql
from app import app
from tables import Results
from tablestwo import Resultb
from db_config import mysql
import re
from flask import flash, render_template, request, redirect

import sys
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/new_user')
def add_user_view():
	"""
	:return: redircts to add.html
	on click function, it triggers when "Add location" option is clicked in the home page
	"""
	return render_template('add.html')

@app.route('/new_spaceship')
def add_spaceship_view():
	"""
	:return: redircts to spaceship table page
	on click function, it triggers when "Add spaceship" option is clicked in the home page
	"""
	return render_template('addspaceships.html')
@app.route('/new_travel')
def travel_view():
	"""
	:return: redircts to travel page
	on click function, it triggers when "travel" option is clicked in the home page

	"""

	return render_template('travel.html')

@app.route('/viewspaceships')
def spaceships_view():
	"""
	:pram: none
	:return: redircts to the spaceship table page
	Displays all space ship in table form
	"""
	conn = None
	cursor = None
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT spaceship.spaceid,spaceship.name,spaceship.model,spaceship.status,locations.city_name,locations.planet_name FROM spaceship INNER JOIN locations ON locations.id=spaceship.locationid")
	rows = cursor.fetchall()
	table = Resultb(rows)
	table.border = True
	return render_template('spaceships.html', table=table)


@app.route('/add', methods=['POST'])
def add_user():
	"""
	 :param : None
     :return: (redircts to the spaceship page)
	 this function adds the location taken from html form user.html
	"""
	conn = None
	cursor = None
	try:		
		_id = request.form['inputId']
		_incity = request.form['inputCity']
		_inplanet = request.form['inputPlanet']
		_incapacity = request.form['inputCapacity']

		# validate the received values
		if _id and _incity and _inplanet and _incapacity and request.method == 'POST':
			#do not save password as a plain text

			# save edits
			sql = "INSERT INTO locations(ID, city_name, planet_name,capacity) VALUES(%s, %s, %s,%s)"
			data = (_id, _incity, _inplanet,_incapacity,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Location added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		flash('Please enter another ID')
		return redirect('/')
	except Exception as TypeError:
		flash('Please enter another ID')
		return redirect('/')
	finally:
		cursor.close() 
		conn.close()

@app.route('/addspaceship', methods=['POST'])
def add_spaceship():
	"""
	:param : None
     :return: (redircts to the add spaceship page)
	this function adds the spaceship taken from html form user.html
	"""
	conn = None
	cursor = None
	try:
		_spaceid = request.form['spaceId']
		_locationid = request.form['locationId']
		_name = request.form['name']
		_model = request.form['model']
		_status = request.form['status']

		# validate the received values
		if _spaceid and _locationid and _name and _model and _status and request.method == 'POST':
			#do not save password as a plain text

			# save edits
			try:
			 	sql = "INSERT INTO spaceship (spaceid, locationid, name,model,status) VALUES(%s, %s, %s,%s,%s)"
			 	data = (_spaceid, _locationid, _name,_model,_status,)
			 	conn = mysql.connect()
			 	cursor = conn.cursor()
			 	cursor.execute(sql, data)
			 	conn.commit()
			 	flash('Spaceship added successfully!')
			 	return redirect('/')
			except Exception as TypeError:
				flash('You have entered invalid locationid or spaceid either spaceid is taken or locationid dosnt exist')
				return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)

	finally:
		cursor.close()
		conn.close()
		
@app.route('/')
def users():
	"""
	:param : None
    :return: (redircts to the home page)
		this function displays all the locations
		"""
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM locations")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/editspaceship/<int:id>')
def edit_view_spaceship(id):
	conn = None
	cursor = None
	"""
	:param : None
    :return: (redircts to the editspaceship.html page)
	this function is used to pass the ID when edit button is clicked when spaceship table is viewed.
	"""
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM spaceship WHERE spaceid=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('editspaceship.html', row=row)
		else:
			return 'Error loading #{spaceid}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/edit/<int:id>')
def edit_view(id):
	conn = None
	cursor = None
	"""
	 :param : None
     :return: (redircts to the travel.html page)
	this function is used to pass the ID when edit button is clicked when location table is viewed.
	"""
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM locations WHERE ID=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/update', methods=['POST'])
def update_user():
	conn = None
	cursor = None
	"""
	 :param : None
     :return: (redircts to the location table page)
	 code for update form of locations
	"""
	try:
		_incity = request.form['inputCity']
		_inplanet = request.form['inputPlanet']
		_incapacity = request.form['inputCapacity']
		_id = request.form['id']
		# validate the received values
		if _incity and _inplanet and _incapacity and _id and request.method == 'POST':
			#do not save password as a plain text

			# save edits
			sql = "UPDATE locations SET city_name=%s, planet_name=%s, capacity=%s WHERE ID=%s"
			data = (_incity, _inplanet, _incapacity, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('location updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/updatespaceship', methods=['POST'])
def update_spaceship():
 conn = None
 cursor = None
 """
  :param : None
  :return: (redircts to the spaceship page)
 Update status of spaceships
 """
 _inStatus = request.form['inputStatus']
 _inStatus=_inStatus.lower()
 _id = request.form['id']
 if _inStatus and _id and request.method == 'POST':

     sql = "UPDATE spaceship SET status=%s WHERE SPACEID=%s"
     data = (_inStatus, _id,)
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute(sql, data)
     conn.commit()
     flash('User updated successfully!')
     return redirect('/viewspaceships')

 else:
	    return 'Error while updating user'


@app.route('/travelpaceship', methods=['POST'])
def travel_spaceship():

 conn = None
 cursor = None
 """
 :param : None
 :return: (redircts to the travel.html page)
 Method used for travel form. 
 First it uses select query to check capacity and status of the spaceship and location. 
 Following checks are applied
 first it checks if the status is operational
 than it checks if the capacity is not equal to zero
 If above condition passed than following changes are made
 (1) Capacity from the departed location increases
 (2) Capacity from the arrival location decreases by 1
 (3) Current location of the spaceship is chaneged by assigning the forgien key
 """
 _idspace = request.form['spaceID']
 _idlocation = request.form['locationID']
 if _idspace and _idlocation and request.method == 'POST':


			sqlcapacity = "SELECT capacity from locations where id=%s"
			sqlstatus= "SELECT status from spaceship where spaceid=%s"
			data = (_idlocation,)
			datat=(_idspace,)
			conn = mysql.connect()
			connt=mysql.connect()
			cursor = conn.cursor()
			cusoro=connt.cursor()
			cursor.execute(sqlcapacity, data)
			cusoro.execute(sqlstatus,datat)
			datarrayt=cursor.fetchall()
			dataarray = cusoro.fetchall()
			stat=str(dataarray)
			cap=str(datarrayt)
			d=re.findall(r'\d+', cap)
			print((d[0]), file=sys.stdout)
			conn.commit()
			if( not 'operational' in stat):
				flash('Spaceship not operational')
				return redirect('/new_travel')

			elif '0' in cap:
				flash('No capacity left!')
				return redirect('/new_travel')
			else:
				sql = "SELECT locationid from spaceship where spaceid=%s"

				data = (_idspace,)
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute(sql, data)
				datarrayt = cursor.fetchall()


				cap = str(datarrayt)
				d = re.findall(r'\d+', cap)
				sqltwo ="UPDATE locations SET capacity=capacity+1 WHERE ID=%s"
				datat = (d[0],)
				connb = mysql.connect()
				cursorb = connb.cursor()
				cursorb.execute(sqltwo,datat)
				connb.commit()

				sql = "UPDATE locations SET capacity=capacity-1 WHERE ID=%s"
				data = (_idlocation,)
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute(sql, data)
				conn.commit()
				sql = "UPDATE spaceship SET locationid=%s WHERE spaceid=%s"
				data = (_idlocation,_idspace,)
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute(sql, data)
				conn.commit()
				flash('Spaceship travelled please view the tables to check changes')
				return redirect('/new_travel')


			flash('User updated successfully!')
			return redirect('/new_travel')
 else:
			return 'Error while updating user'


@app.route('/deletespaceship/<int:id>')
def delete_user(id):
	"""
	:param id: (taken from
	:return: (HTML homepage)
	deletes location given id
	"""
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM locations WHERE ID=%s", (id,))
		conn.commit()
		flash('Location deleted successfully!')
		return redirect('/')
	except TypeError:
		flash("Can't delete this location please delete all spaceships from it first from the spaceship page. This is due to forgien key constraint")
		return redirect('/')
	except Exception as e:
		flash("Can't delete this location please delete all spaceships from it first from the spaceship page. This is due to forgien key constraint")
		return redirect('/')

	finally:
		cursor.close() 
		conn.close()


@app.route('/delete/<int:id>')
def delete_spaceship_user(id):
	"""

	:param id:  (id of the space ship)
	:return: (redirects to the space ship table page)
    removes the spaceship given the id.
	"""
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM spaceship WHERE spaceid=%s", (id,))
		conn.commit()
		flash('Spaceship deleted successfully!')
		return redirect('/viewspaceships')
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


if __name__ == "__main__":
    app.run()