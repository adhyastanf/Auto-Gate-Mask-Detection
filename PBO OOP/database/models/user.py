
from database.database import execute_querry
from database.database import create_db_connection
from database.secret import pw, db

create_user_table = """
	CREATE TABLE user(
	user_id int primary key auto_increment,
	nama_depan varchar(30) not null,
	nama_belakang varchar(30) not null,
	birth_date date,
	gender boolean not null,
	foto blob,
	nomor_telepon int not null,
	email varchar(50) not null,
	username varchar(50) not null,
	password varchar(50) not null,
	role char(1) not null,
	)
	"""
# connection = create_db_connection("localhost", "root", pw, db)
# execute_querry(connection, create_user_table)


