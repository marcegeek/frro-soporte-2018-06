import pymysql

conn, cur = None, None
try:
    conn = pymysql.connect(host='localhost', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    cur.execute('select * from personas where DNI = %s', 35333123)
    p = cur.fetchone()
    if p is not None:
        print(p)
    else:
        print('No existe persona con el DNI 35333123')
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
