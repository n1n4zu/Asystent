from Blackjack.Krupier import Krupier
from Blackjack.Gracz import Gracz
from Blackjack.Clear import Clear


def blackjack():
    global dob

    while True:
        Clear()

        krupier = Krupier()

        gracz1 = Gracz()

        gracze = [gracz1, krupier]

        for i in gracze:
            krupier.dajKarty(i)

        gracz1.pokaz()
        print()
        krupier.pokaz()

        if gracz1.suma == 21:
            print()

            print('Blackjack!')
            print('Wygrał gracz')

            input()

            continue

        if krupier.suma == 21:
            print()

            print('Blackjack!')

            print('Wygrał krupier')

            input()

            continue

        if gracz1.suma == krupier.suma == 21:
            print()

            print('Blackjack!')

            print('Remis')

            input()

            continue

        while gracz1.wynik() and gracz1.suma < 21:
            dob = input('Dobrać kartę? (tak\\nie)\n')

            if dob == 'tak':
                krupier.dobierzKarte(gracz1)

                Clear()

                gracz1.pokaz()
                print()
                krupier.pokaz()

                gracz1.aktSum()

            elif dob == 'nie':
                while krupier.suma < 18:
                    krupier.dobierzKarte(krupier)
                    krupier.aktSum()

                Clear()

                gracz1.pokaz()
                print()
                krupier.pokaz()

                break

            else:
                Clear()

                gracz1.pokaz()
                print()
                krupier.pokaz()

                continue

        print()

        if not gracz1.wynik():
            print("Przegrałeś")

        else:
            if gracz1.suma > krupier.suma:
                print("Wygrał gracz")

            elif gracz1.suma < krupier.suma <= 21:
                print("Wygrał krupier")

            elif gracz1.suma < krupier.suma > 21:
                print("Wygrał gracz")

            else:
                print("Remis")

        gra = input('Czy chcesz grać dalej? (tak/nie)\n').lower()

        if gra != 'tak':
            break

        krupier.zero(gracz1)
        krupier.zero(krupier)
