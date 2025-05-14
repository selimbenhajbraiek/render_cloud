from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

@app.route('/live/vehicles')
def get_vehicles():
    return jsonify([
        {
            "type": random.choice(["BUS", "TRAM", "TRAIN", "SUBWAY", "FERRY"]),
            "station_id": random.randint(1, 15),
            "timestamp": (datetime.utcnow() - timedelta(minutes=random.randint(0, 300))).isoformat()
        }
        for _ in range(10)
    ])
