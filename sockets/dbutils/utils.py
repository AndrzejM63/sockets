from mysql import connector
from mysql.connector.errors import ProgrammingError
import datetime
import os


def add_row(string):
    params = string.split('|')
    ipStr = params[0]
    cpu = float(params[1])
    ram = int(params[2])
    tstamp = datetime.datetime.strptime(params[3].split('.')[0], '%Y-%m-%d %H:%M:%S')

    cnx = connector.connect(
        user="root",
        password='os.environ['DATABASE_PASSWORD'],
        host="127.0.0.1",
        database="sockets_db"
    )

    cursor = cnx.cursor()

    sql1 = """INSERT INTO Raw VALUES(ip='{}', cpu={}, ram={}, timestamp={})""".format(ipStr, cpu, ram, tstamp)
    print string
    print sql1

    try:
        cursor.execute(sql1)
    except ProgrammingError as e:
        print e

    cursor.close()
    cnx.close()


def statistic_for_ip(ipStr=None):
    cnx = connector.connect(
        user="root",
        password=os.environ['DATABASE_PASSWORD'],
        host="127.0.0.1",
        database="sockets_db"
    )

    cursor = cnx.cursor()
    if ipStr is None:
        ipStr = '*'

    sql1 = """SELECT COUNT(*) FROM Raw WHERE ip={}""".format(ipStr)
    try:
        cursor.execute(sql1)
    except ProgrammingError as e:
        print e

    result = cursor.fetchone()

    cursor.close()
    cnx.close()

    return result[0]

def get_all_db_entries():
    cnx = connector.connect(
        user="root",
        password=os.environ['DATABASE_PASSWORD'],
        host="127.0.0.1",
        database="sockets_db"
    )

    cursor = cnx.cursor()
    if ipStr is None:
        ipStr = '*'

    sql1 = """SELECT * FROM Raw"""
    try:
        cursor.execute(sql1)
    except ProgrammingError as e:
        print e

    for row in cursor:
        print row

    cursor.close()
    cnx.close()



