import pymysql

conn, cur = None, None
try:
    conn = pymysql.connect(host='localhost', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    cur.execute('select IdPersona from personas where DNI = %s', 35333123)
    if cur.rowcount != 0:
        id_persona = cur.fetchone()[0]
        fecha = '2018-03-10'
        cur.execute('select * from personas_pesos where fecha >= %s and IdPersona = %s', (fecha, id_persona))
        if cur.rowcount == 0:
            insert_cmd = 'insert into personas_pesos(IdPersona, Fecha, Peso) values (%s, %s, %s)'
            cur.execute(insert_cmd, (id_persona, fecha, 75))
            conn.commit()
        else:
            print('La persona tiene peso registrado en una fecha posterior o igual')
    else:
        print('La persona no existe')
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
