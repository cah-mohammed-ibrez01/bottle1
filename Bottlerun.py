# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:53:37 2019

@author: Maliha
https://bottlepy.org/docs/dev/tutorial_app.html
"""

import sqlite3
import pandas as pd
import json
from bottle import route, run, debug, template,request, route, run, template, get, post, request, static_file
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
 


dbpath = 'c:\\temp\\todo.db'

@route('/plot')
# User visit here to see plot
def show_plot(filename='test.png'):
	return template('show_plot.tpl', filename=filename)




def populateDB():
	conn = sqlite3.connect(dbpath) # Warning: This file is created in the current directory
	conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
	conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
	conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
	conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
	conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
	conn.commit()
	

@route('/todo')
def todo_list():
	conn = sqlite3.connect(dbpath) 
	c = conn.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return output
	conn.close

@route('/new', method='GET')
@route('/new', method='POST')
def new_item():

	if request.POST.save:

		new = request.POST.task.strip()
		conn = sqlite3.connect(dbpath)
		c = conn.cursor()

		c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
		new_id = c.lastrowid

		conn.commit()
		c.close()
		msg = 'The new task was inserted into the database, the ID is %s' % new_id
		d = { "name": msg, "address": "4 Elm Street" }

		#return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
		output = template('new_task',**d)
		return output		
	else:
		d = { "name": "", "address": "4 Elm Street" }
		output = template('new_task',**d)
		return output
	
@route('/images/<filename:re:.*\.png>')
# Perform calculation, create and return a plot
def make_image(filename):
	x = np.arange(-10,10,0.1)  # Calculation
	y = x**2 + 2*x - 5
	fig = Figure()  # Plotting
	canvas = FigureCanvas(fig)
	ax = fig.add_subplot(211)
	ax.plot(x, y)
	ax.set_title('Plot by Matplotlib')
	ax.grid(True)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	canvas.print_figure(filename)
	return static_file(filename, root='./', mimetype='image/png')


def main():
	pass
	debug(True)
	#run(reloader=True)
	run(host='localhost',port=8080,reloader=True)
	#run()


if __name__ == '__main__':
	main()