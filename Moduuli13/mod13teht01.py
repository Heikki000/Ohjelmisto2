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
        luku = int(luku)

        total = 0
        for n in range(1, luku):
            if luku % n == 0:
                total = total + 1
        if total <= 1:
            vastaus = {
                "Number": luku,
                "isPrime": True
            }
        else:
            vastaus = {
                "Number": luku,
                "isPrime": False
            }

    except ValueError:
        vastaus = {
            "palaute": "Virheellinen syöte, korjaa antamasi osoite"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)



