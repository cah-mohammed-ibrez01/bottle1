# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:53:37 2019

@author: Maliha
"""

import sqlite3
from bottle import route, run, debug

def populateDB():
    conn = sqlite3.connect('c:\\temp\\todo.db') # Warning: This file is created in the current directory
    conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
    conn.commit()


@route('/todo')
def todo_list():
    conn = sqlite3.connect('c:\\temp\\todo.db') 
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)



def main():
    pass
    debug(True)
    #run(reloader=True)
    run()


if __name__ == '__main__':
    main()