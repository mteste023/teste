from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/api")
def api():
    url = "https://www.tipminer.com/br/historico/blaze/bac-bo"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
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
