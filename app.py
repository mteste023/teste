from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/api")
def api():
    url = "https://binhole-bac-bo-brazilian-api.p.rapidapi.com/history"
    headers = {
        "X-RapidAPI-Key": "0c07257e8dmsha69b56748a8a1afp1a39f9jsnf8b438cf1101",  # Substitua pela sua chave real do RapidAPI
        "X-RapidAPI-Host": "binhole-bac-bo-brazilian-api.p.rapidapi.com"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        data = res.json()

        historico = [{
            "player": h["playerTotal"],
            "banker": h["bankerTotal"],
            "winner": h["winner"]
        } for h in data.get("history", [])[:20]]

        return jsonify({"historico": historico})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
