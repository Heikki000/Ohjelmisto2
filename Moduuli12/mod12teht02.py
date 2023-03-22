'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''

#https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
import json
import requests

hakusana = input("Anna kaupunki: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&units=metric&lang=fi&appid=1222a6b253e62a974659744943534962"
#print(pyyntö)  testaamista varten

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        #print(json.dumps(json_vastaus, indent=2))  testaamista varten
        print(f"Antamasi kaupungin säätila on: {json_vastaus['weather'][0]['description']} ja lämpötila {json_vastaus['main']['temp']} °C.")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")

#OpenWeather-säärajapinta muuntaa lämpötilan asteisiin, kun haussa määrittelee yksiköiksi metrijärjestelmän (&units=metric)