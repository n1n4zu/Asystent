class Gracz:
    def __init__(self):
        self.imie = 'Gracz'
        self.suma = 0
        self.karty = []
        self.reka = []

    def aktSum(self):
        self.suma = 0

        if len(self.reka) != 0:
            for i in self.karty:
                self.suma += i

        else:
            self.suma = 0

        return self.suma

    def pokSuma(self):
        self.aktSum()
        print(f'Suma: {self.suma}')

    def pokReke(self):
        print("Ręka:")
        for i in self.reka:
            print(i)

    def pokaz(self):
        print(f'{self.imie}:')

        self.aktSum()
        self.pokReke()

        print(f'Suma: {self.suma}')

    def wynik(self):
        if self.suma <= 21:
            return True
        else:
            return False
