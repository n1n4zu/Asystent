from getpass import getpass
from biblioteki.hash import hash
import os
import platform


LOGIN = 'n1n4zu'
PASSWORD = '1cbda35039e1bdae24f9e7a7132c8aa18b72401b7f5e44edff4ca11389f92214'


def loguj():
    attempts = 3
    while attempts > 0:
        if platform.system() == "Windows":
            os.system('cls')
        elif platform.system() == "Linux":
            os.system('clear')

        if attempts > 0:
            login = input('Login\n>')
            password = getpass('Hasło\n>')

            if login == LOGIN and hash(password) == PASSWORD:
                return True
            else:
                attempts -= 1
        else:
            return False