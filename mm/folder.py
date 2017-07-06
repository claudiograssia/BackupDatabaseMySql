import os
import datetime
from shutil import copyfile

NOW = datetime.datetime.now()
BACKUP_FOLDER = "backup"
FOLDER_DATA = "{0}-{1}-{2}".format(NOW.day, NOW.month, NOW.year)
FULL_BACKUP_FOLDER = BACKUP_FOLDER + "/" + FOLDER_DATA


def check_folder_backup():
    if not os.path.isdir(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)


def check_folder_data():
    if not os.path.isdir(FULL_BACKUP_FOLDER):
        os.makedirs(FULL_BACKUP_FOLDER)


def check_get_folder_base_data(database_name):
    if not os.path.isdir(FULL_BACKUP_FOLDER + "/" + database_name):
        os.makedirs(FULL_BACKUP_FOLDER + "/" + database_name)
    return FULL_BACKUP_FOLDER + "/" + database_name


def move_file(src, dest):
    # remove destination if exists
    if os.path.isfile(dest):
        os.remove(dest)

    # copy running
    copyfile(src, dest)

    # remove src after moving file
    if os.path.isfile(src):
        os.remove(src)
