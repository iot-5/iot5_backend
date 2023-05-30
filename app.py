import pickle

from flask import Flask, request, jsonify

from whereami import aps_to_dict, get_model, sample, get_external_sample, get_train_data, train_model, Predicter, \
    get_label_file, write_data

app = Flask(__name__)
model = None

predicter = Predicter()

@app.route("/train", methods=["POST"])
def train():
    data = request.json
    label = data["name"]
    train_data = data["data"]
    label_path = get_label_file(None, label + ".txt")
    X = []
    y = []
    for sample in train_data:
        write_data(label_path, sample)
        X.append(sample)
        y.append(label)
    train_model(X, y)
    return jsonify({"message": "Training completed"})


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
    app.run()