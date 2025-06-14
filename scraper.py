
import requests
from bs4 import BeautifulSoup
from collections import Counter

URL = "https://www.tipminer.com/br/historico/blaze/bac-bo"

def extrair_resultados():
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    dados = soup.select("div.cell__result")
    valores = [int(d.text.strip()) for d in dados if d.text.strip().isdigit()]

    rodadas = []
    for i in range(0, len(valores) - 3, 4):
        p = valores[i] + valores[i+1]
        b = valores[i+2] + valores[i+3]
        if p > b:
            rodadas.append("Player")
        elif b > p:
            rodadas.append("Banker")
        else:
            rodadas.append("Empate")
    return rodadas

def get_prediction(janela=20):
    historico = extrair_resultados()
    ultimos = historico[:janela][::-1]
    contagem = Counter(ultimos)
    total = sum(contagem.values())

    prob = {
        "Player": round(contagem.get("Player", 0) / total * 100, 2),
        "Banker": round(contagem.get("Banker", 0) / total * 100, 2),
        "Empate": round(contagem.get("Empate", 0) / total * 100, 2),
    }
    prob["Sugerido"] = max(prob, key=prob.get)
    return prob
