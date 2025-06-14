from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def obter_resultados():
    url = 'https://www.tipminer.com/br/historico/blaze/bac-bo'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    resultados_html = soup.find_all('div', class_='cell__result')
    resultados = [int(r.text.strip()) for r in resultados_html[:20]]

    historico = []
    player, banker, empate = 0, 0, 0

    for i in range(0, len(resultados), 2):
        a, b = resultados[i], resultados[i+1]
        if a > b:
            vencedor = "Player"
            player += 1
        elif b > a:
            vencedor = "Banker"
            banker += 1
        else:
            vencedor = "Empate"
            empate += 1
        historico.append({"dado_a": a, "dado_b": b, "vencedor": vencedor})

    total = player + banker + empate
    return {
        "Player": round((player / total) * 100, 1),
        "Banker": round((banker / total) * 100, 1),
        "Empate": round((empate / total) * 100, 1),
        "historico": historico
    }

@app.route("/")
def home():
    return "API Bac Bo funcionando!"

@app.route("/api")
def api():
    try:
        dados = obter_resultados()
        return jsonify(dados)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
