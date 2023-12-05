import requests
import json


def pogoda(miasto):
    host = json.loads(requests.get(f'https://api.weatherapi.com/v1/current.json?key=d37e9525eeea43f59a1190826232610%20&q={miasto}&aqi=no').content)

    rownoleznik = host['location']['lat']
    poludnik = host['location']['lon']
    temperatura = host['current']['temp_c']
    wiatr = host['current']['wind_kph']
    pogoda = host['current']['condition']['text']

    return f"""Temperatura: {temperatura}°C
Wiatr: {wiatr}km/h'
Współrzędne: {rownoleznik}N, {poludnik}E
Pogoda: {pogoda}"""
