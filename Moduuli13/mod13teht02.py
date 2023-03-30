'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
'''
import json
from flask import Flask, Response
import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user1',
        password='sala1',
        autocommit=True
    )
connection = connect_db()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/kenttä/<haku_icao>')

def get_airport(haku_icao):
    query = f"select name, municipality from airport where ident ='{haku_icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        vastaus = {'ICAO': haku_icao, 'Name': result[0], 'Municipality': result[1]}
        return vastaus
    else:
        vastaus = {"palaute": "Virheellinen osoite."}
        return vastaus

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, mimetype="application/json")

if __name__== '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)