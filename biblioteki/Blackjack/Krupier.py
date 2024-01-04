import random

talia = {
    'kier': {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'walet': 10,
        'dama': 10,
        'król': 10,
        'as': [1, 11]
    },
    'trefl': {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'walet': 10,
        'dama': 10,
        'król': 10,
        'as': [1, 11]
    },
    'karo': {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'walet': 10,
        'dama': 10,
        'król': 10,
        'as': [1, 11]
    },
    'pik': {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'walet': 10,
        'dama': 10,
        'król': 10,
        'as': [1, 11]
    }
}

kolory = ['kier', 'trefl', 'karo', 'pik']
wartosci = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'walet', 'dama', 'król', 'as']


class Krupier:
    karty = []
    reka = []

    def __init__(self):
        self.imie = 'Krupier'
        self.suma = 0

    def aktSum(self):
        self.suma = 0

        if len(self.reka) != 0:
            for i in self.karty:
                self.suma += i

        else:
            self.suma = 0

        return self.suma

    def dajKarty(self, zawodnik):
        i = 2

        while i != 0:
            kolor = random.choice(kolory)
            war = random.choice(wartosci)

            if war in talia[kolor]:
                if war == 'as' and zawodnik.suma >= 11:
                    zawodnik.karty.append(talia[kolor][war][0])
                    zawodnik.reka.append(f'({kolor}) {war}')

                    del talia[kolor][war]

                    i -= 1

                elif war == 'as' and zawodnik.suma <= 10:
                    zawodnik.karty.append(talia[kolor][war][1])
                    zawodnik.reka.append(f'({kolor}) {war}')

                    del talia[kolor][war]

                    i -= 1

                else:
                    zawodnik.karty.append(talia[kolor][war])
                    zawodnik.reka.append(f'({kolor}) {war}')

                    del talia[kolor][war]

                    i -= 1

            else:
                pass

        return zawodnik.karty

    def dobierzKarte(self, zawodnik):
        kolor = random.choice(kolory)
        war = random.choice(wartosci)

        while war in talia[kolor]:
            if war in talia[kolor]:
                if war == 'as' and zawodnik.suma >= 11:
                    zawodnik.karty.append(talia[kolor][war][0])
                    zawodnik.reka.append(f'({kolor}) {war}')

                    del talia[kolor][war]
                    break

                elif war == 'as' and zawodnik.suma <= 10:
                    zawodnik.karty.append(talia[kolor][war][1])
                    zawodnik.reka.append(f'({kolor}) {war}')

                    del talia[kolor][war]
                    break

                else:
                    zawodnik.karty.append(talia[kolor][war])
                    zawodnik.reka.append(f'({kolor}) {war}')

                    del talia[kolor][war]
                    break

            else:
                continue

    def pokReke(self):
        print("Ręka:")
        for i in self.reka:
            print(i)

    def pokaz(self):
        print(f'{self.imie}:')
        self.aktSum()
        self.pokReke()
        print(f'Suma: {self.suma}')

    def zero(self, zawodnik):
        kody = {'2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'walet': 10,
                'dama': 10,
                'król': 10,
                'as': [1, 11]}

        zaw_karty_kolor = []
        zaw_karty_war = []

        for i in zawodnik.reka:
            zaw_karty_kolor.append(i.split()[0][1:-1])
            zaw_karty_war.append(i.split()[1])

        for i in range(len(zaw_karty_kolor)):
            talia_kolor = talia.get(zaw_karty_kolor[i], {})

            if zaw_karty_war[i] == 'as':
                talia_kolor.update({zaw_karty_war[i]: [1, 11]})

            else:
                talia_kolor.update({zaw_karty_war[i]: kody[zaw_karty_war[i]]})

            talia[zaw_karty_kolor[i]] = talia_kolor

        zawodnik.karty.clear()
        zawodnik.reka.clear()
        zawodnik.suma = 0

