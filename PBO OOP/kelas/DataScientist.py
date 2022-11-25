from asyncio.windows_events import NULL
from multiprocessing import connection
from sqlite3 import connect
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

from database.database import execute_querry, create_db_connection, getRole, getUserID, connection
from database.secret import pw, db

from kelas.DataHarian import DataHarian
from kelas.User import User

class DataScientist(User):
	
	def get_allData():

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id")
		
		myresult = cursor.fetchall()
		for result in myresult:
			print(result)
		
	def get_allDataByDate(tanggal):

		cursor = connection.cursor()
		cursor.execute("SELECT dataharian.dataharian_id, user.nama_depan, user.nama_belakang, user.email, dataharian.input_at FROM user INNER JOIN dataharian ON user.user_id = dataharian.user_id WHERE input_at = '%s'" %tanggal)
		
		myresult = cursor.fetchall()
		for result in myresult:
			print(result)


	def get_allDataByMonth():
		while True:
			print("1. Januari")
			print("2. Februari")
			print("3. Maret")
			print("4. April")
			print("5. Mei")
			print("6. Juni")
			print("7. Juli")
			print("8. Agustus")
			print("9. September")
			print("10. Oktober")
			print("11. November")
			print("12. Desember")
			print("0. Ke Halaman Sebelumnya")

			pilihbulan = int(input("Pilih bulan apa : "))
			if pilihbulan == 1:
				DataHarian.get_data_januari()
			elif pilihbulan == 2:
				DataHarian.get_data_februari()
			elif pilihbulan == 3:
				DataHarian.get_data_maret()
			elif pilihbulan == 4:
				DataHarian.get_data_april()
			elif pilihbulan == 5:
				DataHarian.get_data_mei()
			elif pilihbulan == 6:
				DataHarian.get_data_juni()
			elif pilihbulan == 7:
				DataHarian.get_data_juli()
			elif pilihbulan == 8:
				DataHarian.get_data_agustus()
			elif pilihbulan == 9:
				DataHarian.get_data_september()
			elif pilihbulan == 10:
				DataHarian.get_data_oktober()
			elif pilihbulan == 11:
				DataHarian.get_data_november()
			elif pilihbulan == 12:
				DataHarian.get_data_desember()
			elif pilihbulan == 0:
				break
			
	def get_allJumlahVisitorByDate(tanggal):

		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(dataharian.dataharian_id) as 'Jumlah Pengunjung' FROM dataharian WHERE input_at = '%s' " %tanggal)
		
		myresult = cursor.fetchone()
		for result in myresult:
			print("JUMLAH PENGUNJUNG PADA TANGGAL", tanggal, "ADALAH", result)

	def get_jumlahVisitorByMonth():
		while True:
			print("1. Januari")
			print("2. Februari")
			print("3. Maret")
			print("4. April")
			print("5. Mei")
			print("6. Juni")
			print("7. Juli")
			print("8. Agustus")
			print("9. September")
			print("10. Oktober")
			print("11. November")
			print("12. Desember")
			print("0. Ke Halaman Sebelumnya")
			pilihbulan = int(input("Pilih bulan apa : "))
			if pilihbulan == 1:
				DataHarian.get_jumlah_januari()
			elif pilihbulan == 2:
				DataHarian.get_jumlah_februari()
			elif pilihbulan == 3:
				DataHarian.get_jumlah_maret()
			elif pilihbulan == 4:
				DataHarian.get_jumlah_april()
			elif pilihbulan == 5:
				DataHarian.get_jumlah_mei()
			elif pilihbulan == 6:
				DataHarian.get_jumlah_juni()
			elif pilihbulan == 7:
				DataHarian.get_jumlah_juli()
			elif pilihbulan == 8:
				DataHarian.get_jumlah_agustus()
			elif pilihbulan == 9:
				DataHarian.get_jumlah_september()
			elif pilihbulan == 10:
				DataHarian.get_jumlah_oktober()
			elif pilihbulan == 11:
				DataHarian.get_jumlah_november()
			elif pilihbulan == 12:
				DataHarian.get_jumlah_desember()
			elif pilihbulan == 0:
				break

		

	

	
