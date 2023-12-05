import os
import platform
import pyttsx3

system = platform.system()


def syntezator(mowa):
    # Inicjalizacja syntezatora mowy
    engine = pyttsx3.init()

    # Odczytanie tekstu
    engine.say(mowa)

    # Zatrzymanie odczytywania
    engine.runAndWait()

