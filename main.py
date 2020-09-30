from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)


import random


app = Flask(__name__)

@app.route("/")
def index():
    headline = random.choice(["Rood", "Groen", "Geel", "Blauw"])
    headline2 = random.choice(["Rechterhand", "rechtervoet", "linkervoet", "linkerhand"])
    return render_template("index.html", headline=headline, headline2=headline2)


app.run('0.0.0.0',8080)
