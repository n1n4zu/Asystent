from biblioteki.Blackjack.Krupier import Krupier
from biblioteki.Blackjack.Gracz import Gracz
from biblioteki.Blackjack.Clear import Clear

global dob


def blackjack():
    while True:
        Clear()

        krupier = Krupier()

        gracz = Gracz()

        krupier.zero(gracz)
        krupier.zero(krupier)

        gracze = [gracz, krupier]

        for i in gracze:
            krupier.dajKarty(i)

        gracz.pokaz()
        print()
        krupier.pokaz()

        if gracz.suma == 21:
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

        if gracz.suma == krupier.suma == 21:
            print()

            print('Blackjack!')

            print('Remis')

            input()

            continue

        while gracz.wynik() and gracz.suma < 21:
            dob = input('Dobrać kartę? (tak\\nie)\n')

            if dob == 'tak':
                krupier.dobierzKarte(gracz)

                Clear()

                gracz.pokaz()
                print()
                krupier.pokaz()

                gracz.aktSum()

            elif dob == 'nie':
                while krupier.suma < 18:
                    krupier.dobierzKarte(krupier)
                    krupier.aktSum()

                Clear()

                gracz.pokaz()
                print()
                krupier.pokaz()

                break

            else:
                Clear()

                gracz.pokaz()
                print()
                krupier.pokaz()

                continue

        print()

        if not gracz.wynik():
            print("Przegrałeś")

        else:
            if gracz.suma > krupier.suma:
                print("Wygrał gracz")

            elif gracz.suma < krupier.suma <= 21:
                print("Wygrał krupier")

            elif gracz.suma < krupier.suma > 21:
                print("Wygrał gracz")

            else:
                print("Remis")

        gra = input('Czy chcesz grać dalej? (tak/nie)\n').lower()

        if gra != 'tak':
            break

        krupier.zero(gracz)
        krupier.zero(krupier)
