from fastapi import FastAPI, Depends, Request
from database import Base, SessionLocal, engine
from models import Users, AlatVerified, DataHarian
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from schemas.User import UserSchema
from schemas.Login import UserLogin
from schemas.Tanggal import Tanggal

import uvicorn
import datetime
from datetime import date

import json
from typing import Dict

Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["http://localhost:3000/login","http://localhost:3000/signup","http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/users", response_model=List[UserSchema])
async def get_users(db:Session=Depends(get_db)):
    return db.query(Users).all()

@app.get("/users/total")
async def get_total_users(db:Session=Depends(get_db)):
    return db.execute("SELECT COUNT(id) as 'jumlah' FROM users").all()
    

@app.get("/users/{id}")
async def get_users_by_id(id:int, db:Session=Depends(get_db)):
    return db.execute("SELECT * FROM users WHERE id = %s" %id).fetchall()


@app.post("/users", response_model=UserSchema)
def input_users(user: UserSchema, db:Session=Depends(get_db)):
    u = Users(
        namadepan = user.namadepan,
        namabelakang = user.namabelakang,
        birthdate = user.birthdate,
        gender = user.gender,
        nomor_telepon = user.nomor_telepon,
        email = user.email,
        username = user.username,
        password = user.password
    )
    db.add(u)
    db.commit()
    return u

@app.post("/users/login")
async def user_login(login: UserLogin,db:Session=Depends(get_db)):
    # login = Users(
    #     email = login.email,
    #     password = login.password,
    # )
    datenow = datetime.datetime.now()
    hasil = db.execute("SELECT id FROM users WHERE email = '%s' and password = '%s' " %(login.email, login.password)).fetchone()
    for i in hasil:
        input = AlatVerified(
            user_id = i,
            login_at = datenow,
            masker = login.masker,
        )
        db.add(input)
        db.commit()
        get_scan_id = db.execute("SELECT scan_id FROM alatverified WHERE user_id = %d ORDER BY scan_id DESC" %i).fetchone()
        for j in get_scan_id:
            getmasker = db.execute("SELECT masker FROM alatverified WHERE scan_id = %d" %j).fetchone()
            for masker in getmasker:
                if masker == 1:
                    db.execute("INSERT INTO dataharian VALUES (null, %d, %d, '%s')" %(j, i, datenow))
                    db.commit()
                    return db.execute("SELECT * FROM dataharian").all()
                else:
                    return "ANDA TIDAK DAPAT MASUK"


@app.get("/dataharian")
async def get_dataharian(db:Session=Depends(get_db)):
    return db.execute("SELECT dataharian.dataharian_id, users.namadepan, users.namabelakang, users.email, dataharian.input_at FROM users INNER JOIN dataharian ON users.id = dataharian.user_id").fetchall()

@app.post("/dataharian/tanggal")
async def get_dataharian(date: Tanggal,db:Session=Depends(get_db)):
    return db.execute("SELECT dataharian.dataharian_id, users.namadepan, users.namabelakang, users.email, dataharian.input_at FROM users INNER JOIN dataharian ON users.id = dataharian.user_id WHERE dataharian.input_at = '%s';" %date.tanggal).fetchall()
    
# @app.get("/dataharian/{tanggal}/jumlah")
# async def get_dataharian(tanggal:str, db:Session=Depends(get_db)):
#     return db.execute("SELECT COUNT(user_id) as 'Jumlah' FROM dataharian WHERE input_at = '%s'" %tanggal).fetchall()

@app.post("/dataharian/tanggal/jumlah")
async def get_dataharian(date: Tanggal, db:Session=Depends(get_db)):
    return db.execute("SELECT COUNT(user_id) as 'Jumlah' FROM dataharian WHERE input_at = '%s'" %date.tanggal).fetchall()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

