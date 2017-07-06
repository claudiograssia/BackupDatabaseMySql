HOST = 'localhost'


class BASE_DATA:
    def __init__(self, title, user, passwd):
        self.title = title
        self.user = user
        self.passwd = passwd


DATABASES = [
    BASE_DATA('LOCALHOST', 'root', 'root')
]
