
from flask import Flask, render_template, jsonify
from scraper import get_prediction

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(get_prediction())
