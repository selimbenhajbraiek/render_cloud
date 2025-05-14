from flask import Flask, jsonify
from datetime import datetime, timedelta
import random
import os

app = Flask(__name__)

@app.route("/live/vehicles")
def get_vehicles():
    vehicles = []
    for _ in range(10):
        vehicles.append({
            "type": random.choice(["BUS", "TRAM", "TRAIN", "SUBWAY", "FERRY"]),
            "station_id": random.randint(1, 15),
            "timestamp": (datetime.now() - timedelta(minutes=random.randint(0, 300))).isoformat()
        })
    return jsonify(vehicles)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT automatically
    app.run(host="0.0.0.0", port=port)
