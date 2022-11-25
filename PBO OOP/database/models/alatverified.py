
from database.database import execute_querry
from database.database import create_db_connection
from database.secret import pw, db

create_alatverified_table = """
CREATE TABLE alatverified(
scan_id int primary key auto_increment,
user_id int not null,
foreign key (user_id) references user(user_id),
login_at datetime not null
masker boolean not null,
)
"""

# connection = create_db_connection("localhost", "root", pw, db)
# execute_querry(connection, create_alatverified_table)