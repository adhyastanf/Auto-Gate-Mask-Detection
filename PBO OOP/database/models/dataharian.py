from database.database import execute_querry
from database.database import create_db_connection
from database.secret import pw, db

create_dataharian_table = """
	CREATE TABLE security(
	dataharian_id int primary key auto_increment,
    scan_id int not null,
    foreign key (scan_id) references alatverified(scan_id),
    user_id int not null,
    foreign key (user_id) references user(user_id),
	input_at date
	)
	"""
# connection = create_db_connection("localhost", "root", pw, db)
# execute_querry(connection, create_user_table)