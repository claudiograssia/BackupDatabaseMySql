from mysql import connector
from mm.ignored import IGNORED_DATABASES


def check_all_databases(host, user, passwd):
    cnx = connector.connect(user=user, password=passwd, host=host)
    databases = []
    cursor = cnx.cursor()
    query = "SHOW DATABASES"
    cursor.execute(query)
    for (data) in cursor:
        c = data[0]
        if c not in IGNORED_DATABASES:
            databases.append(c)
    cursor.close()
    cnx.close
    return databases
