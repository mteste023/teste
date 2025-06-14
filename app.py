from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as origens

@app.route("/api")
def api():
    url = "https://www.tipminer.com/br/historico/blaze/bac-bo"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        resultados = []
        for div in soup.select(".cell__result"):
            texto = div.text.strip()
            if texto.isdigit():
                resultados.append(int(texto))

        return jsonify({"historico": resultados})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
