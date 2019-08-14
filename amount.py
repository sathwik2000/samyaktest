import sqlite3
conn=sqlite3.connect(':memory:')
conn=sqlite3.connect('samyak.db')
cursor=conn.cursor()
cursor.execute('select * from reg')
#cursor.execute('select * from klu ')
u=cursor.fetchall()
at=0
for y in u:
    at=at+y[4]
print(at)
