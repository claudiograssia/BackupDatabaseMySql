from mm.check import check_all_databases

HOST = "localhost"
USER = "root"
PASS = "root"

DATAS = check_all_databases(HOST, USER, PASS)


def test():
    for data in DATAS:
        print(data)


"""
def check_all_databases():
    cnx = mysql.connector.connect(user=USER, password=PASS, host=HOST)
    databases = []
    cursor = cnx.cursor()
    query = ("SHOW DATABASES")
    cursor.execute(query)
    for (data) in cursor:
        c = data[0]
        if c not in ignore_databases:
            databases.append(c)
    cursor.close()
    cnx.close
    return databases
"""
