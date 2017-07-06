import subprocess


def back(data, host, user, passwd):
    process = subprocess.Popen(
        'mysqldump -h {0} --user=\"{1}\" --password=\"{2}\" {3} > {3}.sql'.format(host, user, passwd, data),
        shell=True, )
    process.wait()
