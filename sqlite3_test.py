import sqlite3
conn=sqlite3.connect('dbfile')
cur=conn.cursor()
cur.execute('select name,shares,price from portfolio where account=1245')