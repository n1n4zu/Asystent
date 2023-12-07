from biblioteki.czysc import czysc
from biblioteki.pyperclip import copy


def szyfrowanie(message):
    key = int(input('Podaj klucz szyfrowania\n>'))

    mode = input('Podaj tryb pracy programu(szyfrowanie\\deszyfrowanie)\n>')

    SYMBOLS = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻaąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż1234567890 !?.'

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if mode == 'szyfrowanie':
                translatedIndex = symbolIndex + key
            elif mode == 'deszyfrowanie':
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            translated += symbol

    czysc()

    copy(translated)
    return print(translated)
