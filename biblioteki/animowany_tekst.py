from time import sleep
from os import system
from biblioteki.czysc import czysc


czysc()


def animate_text(text):
    liczba = len(text)
    number_of_characters = 1
    while liczba != 0:
        system('cls')
        print(text[0:number_of_characters])
        number_of_characters += 1
        sleep(1/8) 
        liczba -= 1
