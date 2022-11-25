from asyncio.windows_events import NULL
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

from kelas.User import User
from database.database import execute_querry, create_db_connection, getRole, getUserID, connection
from database.secret import pw, db

def getScanID(user_id):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT scan_id from alatverified WHERE user_id = '%d'" %user_id)
            result = cursor.fetchone()
            return result
        except Error as err:
            print(f"Error : '{err}'")

class Alatverified():


    def checkMasker(email, password):
        datenow = datetime.datetime.now()
        emailuser = email
        passworduser = password
        userid = User.getUserID(emailuser, passworduser)
        for j in userid:
            resultsScanID = getScanID(userid)
            for scan_id in resultsScanID:
                inputdataharian = """
                INSERT INTO dataharian VALUES (null, %d, %d, '%s')
                """
                execute_querry(create_db_connection("localhost", "root", pw, db), inputdataharian %(scan_id, j, datenow))


