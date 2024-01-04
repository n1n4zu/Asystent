from biblioteki.czysc import czysc


def deszyfrowanie(message):
    SYMBOLS = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻaąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż1234567890 !?.'

    czysc()

    for key in range(len(SYMBOLS)):
        translated = ''

        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)

                translated += SYMBOLS[translatedIndex]
            else:
                translated += symbol

        print('Klucz #%s: %s' % (key, translated))
