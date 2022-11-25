from database.database import execute_querry
from database.database import create_db_connection
from database.secret import pw, db

create_security_table = """
	CREATE TABLE security(
	security_id int primary key auto_increment,
    user_id int not null,
    foreign key (user_id) references user(user_id),
	tanggalmasukjabatan date not null,
    tanggalkeluarjabatan date not null,
    gaji int
	)
	"""
# connection = create_db_connection("localhost", "root", pw, db)
# execute_querry(connection, create_user_table)