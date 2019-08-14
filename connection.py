import sqlite3
conn=sqlite3.connect(':memory:')
conn=sqlite3.connect('samyak.db')
cursor=conn.cursor()
cursor.execute("create table reg(id int PRIMARY KEY,name text NOT NULL,mail text NOT NULL,clg text NOT NULL,amount int NOT NULL)")
conn.commit()
cursor.close()
conn.close()
