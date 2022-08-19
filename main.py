import os
import time
from datetime import datetime
import sys

TIME_BORDER = 87000
CHECK_DIRECTORY = r"C:\Users\User\PycharmProjects"
FILE_LOG = r"C:\Users\User\PycharmProjects\pythonProject4\log.txt"
DATA_FORMAT = '%d.%m.%Y %H:%M:%S'


def clear_log():
    file_name = open(FILE_LOG, 'w', encoding='utf8')
    file_name.close()


def find_virus(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            file = os.path.join(root, name)
            if check_file(file):
                add_to_log(file)


def check_file(file):
    current_ts = time.time()
    change_time = get_change_time(file)
    return current_ts - change_time < TIME_BORDER


def get_change_time(file):
    m_time = os.stat(file).st_mtime
    a_time = os.stat(file).st_atime
    c_time = os.stat(file).st_ctime
    return max(m_time, a_time, c_time)


def add_to_log(file):
    adding_string = f'{file} : {datetime.fromtimestamp(get_change_time(file)).strftime(DATA_FORMAT)}\n'
    with open(FILE_LOG, 'a') as file_name:
        file_name.write(adding_string)


if __name__ == '__main__':
    clear_log()
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        find_virus(directory)
    else:
        find_virus(CHECK_DIRECTORY)


