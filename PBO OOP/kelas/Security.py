from asyncio.windows_events import NULL
from multiprocessing import connection
from sqlite3 import connect
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

from database.database import execute_querry, create_db_connection, getRole, getUserID, connection
from database.secret import pw, db

from kelas.User import User

class Security(User):

	def get_peopleNoMask():

		cursor = connection.cursor()
		cursor.execute("SELECT user.user_id, user.nama_depan, user.nama_belakang, alatverified.scan_id, alatverified.masker FROM user INNER JOIN alatverified ON user.user_id = alatverified.user_id WHERE masker = 0;")
		
		myresult = cursor.fetchall()
		for result in myresult:
			print(result)

	def get_peopleNoMaskByDate(tanggal):

		cursor = connection.cursor()
		cursor.execute("SELECT user.user_id, user.nama_depan, user.nama_belakang, alatverified.scan_id, alatverified.masker, alatverified.login_at FROM user INNER JOIN alatverified ON user.user_id = alatverified.user_id WHERE masker = 1 AND login_at > '%s' " %tanggal)
		
		myresult = cursor.fetchall()
		for result in myresult:
			print(result)
			
	def get_peopleWithMask():

		cursor = connection.cursor()
		cursor.execute("SELECT user.user_id, user.nama_depan, user.nama_belakang, alatverified.scan_id, alatverified.masker FROM user INNER JOIN alatverified ON user.user_id = alatverified.user_id WHERE masker = 1;")
		
		myresult = cursor.fetchall()
		for result in myresult:
			print(result)
