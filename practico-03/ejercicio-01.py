import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='MySQL', db='personasdb')
cur = conn.cursor()
cur.execute('select * from personas')
lista_personas = cur.fetchall()
for p in lista_personas:
    print(p)
cur.close()
conn.close()
