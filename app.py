from flask import Flask, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    return jsonify({
        "inside_temp": None,
        "outside_temp": None,
        "humidity": None,
        "pressure": None,
        "voltage": None,
        "current": None,
        "heater": None,
        "fan": None,
        "connected": False,
        "last_update": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == "__main__":
    app.run()
