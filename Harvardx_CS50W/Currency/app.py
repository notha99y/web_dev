import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

load_dotenv()

FIXER_KEY = os.getenv('FIXER_KEY')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")
    print(currency)
    res = requests.get(
        f"http://data.fixer.io/api/latest?access_key={FIXER_KEY}",
        params={"base": "EUR", "symbols": currency},
    )

    if res.status_code != 200:
        return jsonify({"success": False})

    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')