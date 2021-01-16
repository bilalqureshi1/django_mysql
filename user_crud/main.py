import pymysql
from app import app
from tables import Results
from tablestwo import Resultb
from db_config import mysql
from flask import flash, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/new_user')
def add_user_view():
	return render_template('add.html')

@app.route('/new_spaceship')
def add_spaceship_view():
	return render_template('addspaceships.html')


@app.route('/viewspaceships')
def spaceships_view():
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
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/addspaceship', methods=['POST'])
def add_spaceship():
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
			sql = "INSERT INTO spaceship (spaceid, locationid, name,model,status) VALUES(%s, %s, %s,%s,%s)"
			data = (_spaceid, _locationid, _name,_model,_status,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Spaceship added successfully!')
			return redirect('/viewspaceships')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		
@app.route('/')
def users():
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
			flash('User updated successfully!')
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
 _inStatus = request.form['inputStatus']
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

@app.route('/deletespaceship/<int:id>')
def delete_user(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM locations WHERE ID=%s", (id,))
		conn.commit()
		flash('Location deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/delete/<int:id>')
def delete_spaceship_user(id):
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