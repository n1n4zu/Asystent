import requests
import json
from biblioteki.czysc import czysc


def pogoda(miasto):
    host = json.loads(requests.get(
        f'https://api.weatherapi.com/v1/current.json?key=d37e9525eeea43f59a1190826232610%20&q={miasto}&aqi=no').content)

    kraj = host['location']['country']
    rownoleznik = host['location']['lat']
    poludnik = host['location']['lon']
    temperatura = host['current']['temp_c']
    wiatr = host['current']['wind_kph']
    pogoda = host['current']['condition']['text']

    if pogoda == 'Clear':
        pogoda = 'Bezchmurnie'
    elif pogoda == 'Cloud' or pogoda == 'Overcast':
        pogoda = 'Pochmurnie'
    elif pogoda == 'Partly cloudy':
        pogoda = 'Cześciowe zachmurzenie'
    elif pogoda == 'Rain':
        pogoda = 'Pada deszcz'
    elif pogoda == 'Snow':
        pogoda = 'Pada śnieg'
    elif pogoda == 'Mist':
        pogoda = 'Mgła'
    elif pogoda == 'Sunny':
        pogoda = 'Słonecznie'
    elif pogoda == 'Patchy light snow':
        pogoda = 'Lekki śnieg'

    czysc()

    return f"""Miasto: {miasto}
Kraj: {kraj}
Temperatura: {temperatura}°C
Wiatr: {wiatr}km/h
Współrzędne: {rownoleznik}N, {poludnik}E
Pogoda: {pogoda}"""
