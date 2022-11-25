from asyncio.windows_events import NULL
from multiprocessing import connection
from sqlite3 import connect
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

from database.database import execute_querry, create_db_connection, getRole, getUserID, connection
from database.secret import pw, db

class User():
	
	def __init__(self, namadepan, namabelakang, birthdate, gender, nomortelepon, email, username, password):
		self.__namadepan = namadepan
		self.__namabelakang = namabelakang
		self.__birthdate = birthdate
		self.__gender = gender
		self.__nomortelepon = nomortelepon
		self.__email = email
		self.__username = username
		self.__password = password

	def input_biodata(namadepan, namabelakang, birthdate, gender, nomortelepon, email, username, password):
		nama_depan = namadepan
		nama_belakang = namabelakang
		birth_date = birthdate
		gender1 = gender
		nomor_telepon = nomortelepon
		emailuser = email
		usernameuser = username
		passworduser = password
		connection = create_db_connection("localhost", "root", pw, db)
		execute_querry(connection, "INSERT INTO user VALUES(null, '%s', '%s', '%s', %r, NULL, %s, '%s', '%s', '%s', 'user')" %(nama_depan, nama_belakang, birth_date, gender1, nomor_telepon, emailuser, usernameuser, passworduser))


	def userLogin(email, password):
		datenow = datetime.datetime.now()
		emailuser = email
		passworduser = password

		cursor = connection.cursor()
		cursor.execute("select user_id from user where email = '%s' and password = '%s'" %(emailuser, passworduser))

		if cursor.fetchone() == None:
			print("Akun tidak ada")
		else:
			# print("Berhasil Log-in")
			role = """
			select role from user where email = '%s' and password = '%s'
			"""
			resultsRole = getRole(connection, role %(emailuser, passworduser))
			for role in resultsRole:
				if role == None:
					print("User id Tidak ada")
				elif role == 'security':
					print("Anda masuk dengan akun security")
				elif role == 'datascientist':
					print("Anda masuk dengan akun datascientist")
				else:
					resultsID = getUserID(connection, email, password)
					for userid in resultsID:
						masker = int(input("Apakah anda memakai masker : "))
						inputverified = """
						insert into alatverified values (null, '%d', '%s', '%d')
						"""
						execute_querry(connection, inputverified %(userid, datenow, masker))
						print("Anda sudah masuk")
					

	def getUserID(email, password):
		cursor = connection.cursor()
		try:
			cursor.execute("SELECT user_id from user where email = '%s' and password = '%s'" %(email, password))
			result = cursor.fetchone()
			return result
		except Error as err:
			print(f"Error : '{err}'") 

	def getVerifiedID(connection, querry):
		cursor = connection.cursor()
		try:
			cursor.execute(querry)
			result = cursor.fetchone()
			return result
		except Error as err:
			print(f"Error : '{err}'")

	def getRole(connection, email, password):
		cursor = connection.cursor()
		try:
			cursor.execute("SELECT role from user where email = '%s' and password = '%s'" %(email, password))
			result = cursor.fetchone()
			return result
		except Error as err:
			print(f"Error : '{err}'")

	def get_namadepan(self):
		return self.__namadepan

	def get_namabelakang(self):
		return self.__namabelakang

	def get_birthdate(self):
		return self.__birthdate

	def get_gender(self):
		return self.__gender

	def get_nomortelepon(self):
		return self.__nomortelepon

	def get_email(self):
		return self.__email

	def get_username(self):
		return self.__username

	def get_password(self):
		return self.__password
