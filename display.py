import sqlite3
conn=sqlite3.connect(':memory:')
conn=sqlite3.connect('samyak.db')
cursor=conn.cursor()
cursor.execute('select * from reg')
#cursor.execute('select * from klu ')
u=cursor.fetchall()
for y in u:
    print(y[0],y[1],y[2],y[3],y[4])
