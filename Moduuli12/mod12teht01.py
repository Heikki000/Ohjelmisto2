'''
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
'''
import json
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()
print(json.dumps(vastaus, indent=2))

for a in vastaus:
    print(a["value"])