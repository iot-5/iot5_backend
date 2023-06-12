from flask import Flask, request, jsonify

from path2 import result_cli
from whereami import *

app = Flask(__name__)

predicter = Predicter()

@app.route('/train', methods=['POST'])
def learn_endpoint():
    data = request.get_json()
    name = data.get('name')
    ap_data = data.get('data')
    ap_dict = aps_to_dict(ap_data)
    learn(name, data=ap_dict)
    return jsonify({'message': 'Learning complete'})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"]
    aps = []
    for item in data:
        ssid = item["ssid"]
        bssid = item["bssid"]
        quality = item["quality"]
        aps.append({"ssid": ssid, "bssid": bssid, "quality": quality})
    location = predicter.predict(aps)
    return jsonify({"location": location})

@app.route('/path', methods=['POST'])
def find_path():
    data = request.get_json()
    start = data['start']
    end = data['end']
    final_path, initial_pos = result_cli(start, end)
    if initial_pos == 0:
        start_direct = "Left"
    elif initial_pos == 1:
        start_direct = "Right"
    else:
        start_direct = "None-개발중"

    response = {
        "start_direction": start_direct,
        "path": final_path
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
