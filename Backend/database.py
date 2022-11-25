from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/gatesystem")

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, bind=engine)
