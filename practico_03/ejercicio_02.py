import pymysql

conn, cur = None, None
try:
    conn = pymysql.connect(host='localhost', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    insert_cmd = 'insert into personas(Nombre, FechaNacimiento, DNI, Altura) values (%s, %s, %s, %s)'
    cur.execute(insert_cmd, ('Roberto', '1991-01-18', 35333123, 170))
    conn.commit()
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
