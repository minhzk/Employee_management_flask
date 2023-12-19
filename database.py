from flask import g 
import sqlite3 

def connect_to_database():
    sql = sqlite3.connect('E:/code/Py/employee_management/employee.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_database():
    if not hasattr(g, 'employee_db'):
        g.employee_db = connect_to_database()
    return g.employee_db