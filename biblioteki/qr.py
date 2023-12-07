import pyqrcode
import png


def qr(url):
    qr = pyqrcode.create(url)

    nazwa = input('Podaj nazwe pliku: \n>')

    qr.png(f'QR/{nazwa}.png', scale=8)

    print(f'Zapisano plik {nazwa}.png')
