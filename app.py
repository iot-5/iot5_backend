from flask import Flask, request, jsonify

from whereami import *

app = Flask(__name__)

predicter = Predicter()

@app.route('/learn', methods=['POST'])
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
