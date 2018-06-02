import pymysql

conn, cur = None, None
try:
    conn = pymysql.connect(host='localhost', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    update_cmd = 'update personas set Nombre = %s, FechaNacimiento = %s, Altura = %s where DNI = %s'
    cur.execute(update_cmd, ('Roberto Martínez', '1991-01-18', 170, 35333123))
    conn.commit()
    cur.execute('select * from personas where DNI = %s', 35333123)
    p = cur.fetchone()
    print(p)
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
