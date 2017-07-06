from mm.databases import HOST, DATABASES
from mm.check import check_all_databases
from mm.backup import back
from mm.folder import check_folder_backup, check_folder_data, check_get_folder_base_data, move_file
import os
import time
import datetime


def main():
    check_folder_backup()
    check_folder_data()
    for data in DATABASES:
        try:
            database_folder = check_get_folder_base_data(data.user)
            databases_user = check_all_databases(HOST, data.user, data.passwd)
            for database_user in databases_user:
                back(database_user, HOST, data.user, data.passwd)
                sql_file = database_user + ".sql"
                src = os.getcwd() + "/" + sql_file

                max_time = 60
                cur_time = 0
                prev_size = 0
                while True:
                    if cur_time >= max_time:
                        raise Exception("Ci ho messo troppo tempo per fare il backup di: {0}".format(data.title))
                    cur_time += 1
                    if not os.path.isfile(src):
                        time.sleep(1)
                        continue
                    cur_size = os.stat(src)
                    if cur_size == 0:
                        time.sleep(1)
                        continue
                    if cur_size != prev_size:
                        prev_size = cur_size
                        time.sleep(3)
                        continue
                    else:
                        break

                move_file(src, os.getcwd() + "/" + database_folder + "/" + sql_file)
        except Exception as err:
            print("{0} :: {1}".format(datetime.datetime.now(), err.args), file=open("error.log", "a"))


if __name__ == '__main__':
    main()
