from kelas.User import User
from kelas.Alatverified import Alatverified
from kelas.DataScientist import DataScientist
from kelas.Security import Security

from database.database import connection
import datetime
from datetime import date


while True:
    print("1. Registrasi Akun")
    print("2. Login")
    print("0. Exit")
    pilihan = int(input("Masukkan pilihan : "))
    if pilihan == 1:
        namadepan = input("Masukkan nama depan anda : ")
        nama_belakang = input("Masukkan nama belakang anda : ")
        birth_date = input("Masukkan tanggal lahir anda : ")
        gender = input("Masukkan jenis kelamin (M=1/F=0) : ")
        nomor_telepon = int(input("Masukkan nomor telefon anda : "))
        email = input("Masukkan email anda : ")
        username = input("Masukkan username anda : ")
        password = input("Masukkan password anda : ")
        User.input_biodata(namadepan, nama_belakang, birth_date, True, nomor_telepon, email, username, password)
        
    elif pilihan == 2 :
        email = input("Masukkan email anda : ")
        password = input("Masukkan password anda : ")
        User.userLogin(email, password)
        hasilrole = User.getRole(connection, email, password)
        for role in hasilrole:
            if role == 'user':
                Alatverified.checkMasker(email, password)
            elif role == 'security':
                print("1. Check Data People Tidak Pakai Masker")
                print("2. Check Data People Tidak Pakai Masker By Date")
                print("3. Check Data People Pakai Masker")
                while True:
                    choose = int(input("Masukkan pilihan : "))
                    if choose == 1:
                        Security.get_peopleNoMask()
                    elif choose == 2:
                        tanggal = input("Masukkan tanggal : ")
                        Security.get_peopleNoMaskByDate(tanggal)
                    elif choose == 3:
                        Security.get_peopleWithMask()
                    else:
                        break
            elif role == 'datascientist':
                while True:
                    print("1. Check Data Information of Visitors")
                    print("2. Check Data Information of Visitors By Date")
                    print("4. Check Data Information of Visitors By Month")
                    print("3. Check Jumlah Pengunjung By Date")
                    print("5. Check Jumlah Pengunjung By Month")
                    print("6. Log Out")
                    choose = int(input("Masukkan pilihan : "))
                    if choose == 1:
                        DataScientist.get_allData()
                    elif choose == 2:
                        tanggal = input("Masukkan tanggal : ")
                        DataScientist.get_allDataByDate(tanggal)
                    elif choose == 3:
                        DataScientist.get_allDataByMonth()
                    elif choose == 4:
                        tanggal = input("Masukkan tanggal : ")
                        DataScientist.get_allJumlahVisitorByDate(tanggal)
                    elif choose == 5:
                        DataScientist.get_jumlahVisitorByMonth()
                    elif choose == 6:
                        break
    elif pilihan == 0:
        break
                    
                    
        
