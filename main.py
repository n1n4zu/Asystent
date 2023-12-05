import os
import platform
import psutil
from biblioteki.pogoda import pogoda
from biblioteki.menu import menu
from biblioteki.loguj import loguj
from biblioteki.caesarCipher import szyfrowanie
from biblioteki.caesarHacker import deszyfrowanie
from biblioteki.syntezator import syntezator
from biblioteki.wylacz import zamknij
from biblioteki.programy import program
from biblioteki.czysc import czysc
from webbrowser import open
import subprocess


global opcja


def main():
    global opcja
    czysc()

    if loguj():
        while True:
            czysc()

            menu()

            print()

            opcja = input('Co chcesz zrobić?\n>')

            match opcja:
                case 'wyłącz system':
                    zamknij()
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

                    program(programy)
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

                case 'wyloguj':
                    break

                case 'wyjdź':
                    break

                case _:
                    print('Nie wybrano właściwej opcji')
                    input()

    if opcja == 'wyloguj':
        opcja = ''
        main()


main()
