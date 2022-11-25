from asyncio.windows_events import NULL
from multiprocessing import connection
from sqlite3 import connect
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

from database.database import execute_querry, create_db_connection, getRole, getUserID, connection
from database.secret import pw, db

class DataHarian():

	def get_data_januari():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-01-01' AND input_at < '2022-02-01' ")
		
		januari = cursor.fetchall()
		for hasil in januari:
			print(hasil)

	def get_data_februari():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-02-01' AND input_at < '2022-03-01' ")
		
		februari = cursor.fetchall()
		for hasil in februari:
			print(hasil)

	def get_data_maret():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-03-01' AND input_at < '2022-04-01' ")
		
		maret = cursor.fetchall()
		for hasil in maret:
			print(hasil)

	def get_data_april():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-04-01' AND input_at < '2022-05-01' ")
		
		april = cursor.fetchall()
		for hasil in april:
			print(hasil)
	
	def get_data_mei():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-05-01' AND input_at < '2022-06-01' ")
		
		mei = cursor.fetchall()
		for hasil in mei:
			print(hasil)

	def get_data_juni():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-06-01' AND input_at < '2022-07-01' ")
		
		juni = cursor.fetchall()
		for hasil in juni:
			print(hasil)


	def get_data_juli():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-07-01' AND input_at < '2022-08-01' ")
		
		juli = cursor.fetchall()
		for hasil in juli:
			print(hasil)

	def get_data_agustus():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-08-01' AND input_at < '2022-09-01' ")
		
		agustus = cursor.fetchall()
		for hasil in agustus:
			print(hasil)

	def get_data_september():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-09-01' AND input_at < '2022-10-01' ")
		
		september = cursor.fetchall()
		for hasil in september:
			print(hasil)

	def get_data_oktober():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-10-01' AND input_at < '2022-11-01' ")
		
		oktober = cursor.fetchall()
		for hasil in oktober:
			print(hasil)

	def get_data_november():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-11-01' AND input_at < '2022-12-01' ")
		
		november = cursor.fetchall()
		for hasil in november:
			print(hasil)

	def get_data_desember():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-12-01' AND input_at < '2023-01-01' ")
		
		desember = cursor.fetchall()
		for hasil in desember:
			print(hasil)

	def get_jumlah_januari():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-01-01' AND input_at < '2022-02-01' ")
		
		januari = cursor.fetchall()
		for hasil in januari:
			print(hasil)

	def get_jumlah_februari():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-02-01' AND input_at < '2022-03-01' ")
		
		februari = cursor.fetchall()
		for hasil in februari:
			print(hasil)

	def get_jumlah_maret():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-03-01' AND input_at < '2022-04-01' ")
		
		maret = cursor.fetchall()
		for hasil in maret:
			print(hasil)

	def get_jumlah_april():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-04-01' AND input_at < '2022-05-01' ")
		
		april = cursor.fetchall()
		for hasil in april:
			print(hasil)

	def get_jumlah_mei():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-05-01' AND input_at < '2022-06-01' ")
		
		mei = cursor.fetchall()
		for hasil in mei:
			print(hasil)

	def get_jumlah_juni():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-06-01' AND input_at < '2022-07-01' ")
		
		juni = cursor.fetchall()
		for hasil in juni:
			print(hasil)

	def get_jumlah_juli():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-07-01' AND input_at < '2022-08-01' ")
		
		juli = cursor.fetchall()
		for hasil in juli:
			print(hasil)

	def get_jumlah_agustus():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-08-01' AND input_at < '2022-09-01' ")
		
		agustus = cursor.fetchall()
		for hasil in agustus:
			print(hasil)

	def get_jumlah_september():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-10-01' AND input_at < '2022-11-01' ")
		
		september = cursor.fetchall()
		for hasil in september:
			print(hasil)

	def get_jumlah_oktober():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-11-01' AND input_at < '2022-12-01' ")
		
		oktober = cursor.fetchall()
		for hasil in oktober:
			print(hasil)

	def get_jumlah_november():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-12-01' AND input_at < '2023-01-01' ")
		
		november = cursor.fetchall()
		for hasil in november:
			print(hasil)

	def get_jumlah_desember():

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian_id) as 'Jumlah Data : ' FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at > '2022-01-01' AND input_at < '2022-02-01' ")
		
		desember = cursor.fetchone()
		for hasil in desember:
			print(hasil)

	

	
