import pymysql
from datetime import datetime
import json

conn, cur = None, None
try:
    conn = pymysql.connect(host='localhost', user='personas_user', passwd='personas', db='personasdb')
    cur = conn.cursor()
    cur.execute('select * from personas')
    lista_personas = cur.fetchall()
    lista_simple = []
    for p in lista_personas:
        cur.execute('select Fecha, Peso from personas_pesos where IdPersona = %s', p[0])
        pesos = cur.fetchall()
        lista_simple.append([])
        for e in p:
            if type(e) != datetime:
                lista_simple[-1].append(str(e))
            else:
                lista_simple[-1].append(str(e.date()))
        lista_simple[-1].append([])
        for pes in pesos:
            lista_simple[-1][-1].append((str(pes[0]), str(pes[1])))
    print(json.JSONEncoder().encode(lista_simple))
except Exception as err:
    print('Error: ', err)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
