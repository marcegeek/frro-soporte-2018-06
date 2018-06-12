import pymysql

conn, cur = None, None
try:
    conn = pymysql.connect(host='localhost', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    delete_cmd = 'delete from personas where DNI = %s'
    if cur.execute(delete_cmd, 35333123) != 0:
        print('Eliminada la persona con DNI 35333123')
    else:
        print('No existe persona con DNI 35333123')
    conn.commit()
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
