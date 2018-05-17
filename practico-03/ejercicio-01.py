import pymysql

conn, cur = None, None
try:
    conn = pymysql.connect(host='www.db4free.net', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    cur.execute('select * from personas')
    lista_personas = cur.fetchall()
    for p in lista_personas:
        print(p)
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
