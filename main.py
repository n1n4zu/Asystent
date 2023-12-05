import os
import platform
import psutil
from biblioteki.pogoda import pogoda
from biblioteki.menu import menu
from biblioteki.loguj import loguj
from biblioteki.caesarCipher import szyfrowanie
from biblioteki.caesarHacker import deszyfrowanie
from biblioteki.syntezator import syntezator
from webbrowser import open
import subprocess


def main():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')

    if loguj():
        while True:
            if platform.system() == "Windows":
                os.system('cls')
            elif platform.system() == "Linux":
                os.system('clear')

            menu()

            print()

            opcja = input('Co chcesz zrobić?\n>')

            match opcja:
                case 'wyłącz system':
                    PROGRAMY = ['pycharm64.exe', 'cmd.exe', 'asystent.exe', 'terminal', 'pycharm64']
                    if platform.system() == "Windows":
                        os.system('shutdown /s /t 10')
                        for program in PROGRAMY:
                            for proc in psutil.process_iter(['pid', 'name']):
                                if program.lower() in proc.info['name'].lower():
                                    try:
                                        os.kill(proc.info['pid'], 9)
                                        print(f"Zamknięto {proc.info['name']} (PID: {proc.info['pid']})")
                                    except PermissionError as e:
                                        print(e)
                        break

                    elif platform.system() == "Linux":
                        os.system('poweroff')
                        for program in PROGRAMY:
                            for proc in psutil.process_iter(['pid', 'name']):
                                if program.lower() in proc.info['name'].lower():
                                    try:
                                        os.kill(proc.info['pid'], 9)
                                        print(f"Zamknięto {proc.info['name']} (PID: {proc.info['pid']})")
                                    except PermissionError as e:
                                        print(e)
                        break

                case 'jaka jest pogoda':
                    miasto = input('Jakie miasto?\n>')
                    try:
                        print(pogoda(miasto))
                    except:
                        print('Miasto nie jest obsługiwane przez stacje badawcze')
                    input()

                case 'włącz youtube':
                    open('https://www.youtube.com')

                case 'włącz youtube music':
                    open('https://music.youtube.com/')

                case 'włącz github':
                    open('https://github.com/')

                case 'uruchom steam':
                    subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe")

                case 'zamknij programy':
                    programy = []
                    pro = input('Pierwszy program\n>')

                    if pro[-4:] == '.exe':
                        programy.append(pro)
                    else:
                        programy.append(pro + '.exe')

                    while pro != '':
                        pro = input('Następny program(Jeśli podałeś wszystkie, wciśnij Enter)\n>')

                        if pro != '':
                            if pro[-4:] == '.exe':
                                programy.append(pro)
                            else:
                                programy.append(pro + '.exe')

                    for program in programy:
                        for proc in psutil.process_iter(['pid', 'name']):
                            if program.lower() in proc.info['name'].lower():
                                try:
                                    os.kill(proc.info['pid'], 9)
                                    print(f"Zamknięto {proc.info['name']} (PID: {proc.info['pid']})")
                                except PermissionError as e:
                                    print(e)
                    input()

                case 'szyfrowanie':
                    message = input('Podaj tekst\n>')
                    szyfrowanie(message)
                    input()

                case 'deszyfrowanie':
                    message = input('Podaj szyfr do złamania\n>')
                    deszyfrowanie(message)
                    input()

                case 'syntezator':
                    message = input('Podaj szyfr do złamania\n>')
                    syntezator(message)

                case 'wyjdź':
                    break

                case _:
                    print('Nie wybrano właściwej opcji')
                    input()


main()
