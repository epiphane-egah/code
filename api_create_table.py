import sqlite3


# connection base de données
db = sqlite3.connect("database.db")
c = db.cursor()

# CREATE SEQUENCE seq_users START = 1 INCREMENT = 1;
# DEFAULT seq_users.NEXTVAL
# IDENTITY
query = '''CREATE TABLE IF NOT EXISTS article (
id integer primary key AUTOINCREMENT,
name varchar(60) not null,
description varchar(120),
price int
)
'''

c.execute(query)
db.commit()
db.close
