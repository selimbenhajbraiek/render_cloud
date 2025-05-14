from flask import Flask, jsonify
from datetime import datetime, timedelta
import random
import os

app = Flask(__name__)

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

mock_data = []
mock_stations =[]

@app.route("/live/vehicles", methods=["GET"])
def get_vehicles():
    return jsonify(mock_data)
@app.route("/live/stations", methods=["POST"])
def add_station():
    station = request.json
    station["timestamp"] = station.get("timestamp") or datetime.now().isoformat()
    mock_stations.append(station)
    return jsonify({"message": "Station added", "station": station})

@app.route("/live/stations", methods=["GET"])
def get_stations():
    return jsonify(mock_stations)
@app.route("/live/vehicles", methods=["POST"])
def add_vehicle():
    vehicle = request.json
    vehicle["timestamp"] = vehicle.get("timestamp") or datetime.now().isoformat()
    mock_data.append(vehicle)
    return jsonify({"message": "Vehicle added", "vehicle": vehicle})

@app.route("/live/vehicles", methods=["DELETE"])
def clear_vehicles():
    global mock_data
    mock_data = []
    return jsonify({"message": "Mock data cleared"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT automatically
    app.run(host="0.0.0.0", port=port)
