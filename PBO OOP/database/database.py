from asyncio.windows_events import NULL
from multiprocessing import connection
from sqlite3 import connect
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

pw = "1234"
db = "autogatesystem"

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("My SQL Database connection succesful")
    except Error as err:
        print(f"Error : '{err}'")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database create succesfully")
    except Error as err:
        print(f"Error : '{err}' ")

#create_database_querry = "CREATE DATABASE percobaan"
#create_database(connection, create_database_querry)

def create_db_connection(host_name, user_name, user_password, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = database_name
        )
        print("MySQL database connection succesfully")
    except Error as err:
        print(f"Error : '{err}")
    return connection

def execute_querry(connection, querry):
    cursor = connection.cursor()
    try:
        cursor.execute(querry)
        connection.commit()
        print("Query was successfully")
    except Error as err:
        print(f"Error : '{err}'")


connection = create_db_connection("localhost", "root", pw, db)

def getUserID(connection, email, password):
		cursor = connection.cursor()
		try:
			cursor.execute("SELECT user_id from user where email = '%s' and password = '%s'" %(email, password))
			result = cursor.fetchone()
			return result
		except Error as err:
			print(f"Error : '{err}'") 


def getRole(connection, querry):
    cursor = connection.cursor()
    try:
        cursor.execute(querry)
        result = cursor.fetchone()
        return result
    except Error as err:
        print(f"Error : '{err}'")