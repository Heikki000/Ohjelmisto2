'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
'''
import json
from flask import Flask, Response

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def is_prime(luku):
    try:
        number = int(input("Anna luku: "))
        is_prime = True

        for n in range(2, number):
            if number % n == 0:
                print(f"{number} ei ole alkuluku.")
                is_prime = False
                break

        # if is_prime == true:
        if is_prime:
            print(f"\n{number} on alkuluku.")
