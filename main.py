from biblioteki.loguj import loguj
from biblioteki.ip import ip
from biblioteki.pogoda import pogoda
from biblioteki.menu import menu
from biblioteki.caesarCipher import szyfrowanie
from biblioteki.caesarHacker import deszyfrowanie
from biblioteki.qr import qr
from biblioteki.syntezator import syntezator
from biblioteki.wylacz import zamknij
from biblioteki.programy import program
from biblioteki.czysc import czysc
from webbrowser import open
from biblioteki.blackjack import blackjack


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

            match opcja.lower():
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

                case 'włącz twitch':
                    open('https://twitch.tv/')

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

                case 'brute force':
                    message = input('Podaj szyfr do złamania\n>')
                    deszyfrowanie(message)
                    input()

                case 'syntezator':
                    message = input('Co mam powiedzieć?\n>')
                    syntezator(message)

                case 'zdobądź adres ip':
                    print(ip())
                    input()

                case 'wygeneruj kod qr':
                    url = input('Podaj adres url\n>')
                    qr(url)
                    input()

                case 'blackjack':
                    blackjack()

                case 'wyloguj':
                    break

                case 'wyjdź':
                    czysc()
                    break

                case _:
                    print('Nie wybrano właściwej opcji')
                    input()

    if opcja == 'wyloguj':
        opcja = ''
        main()


main()
