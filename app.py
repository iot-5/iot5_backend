import pickle

from flask import Flask, request, jsonify

from whereami import aps_to_dict, get_model, sample, get_external_sample, get_train_data, train_model, Predicter, \
    get_label_file, write_data, ensure_whereami_path, learn

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


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/learn", methods=["POST"])
def learn_api():
    data = request.json
    label = data["name"]
    train_data = data["data"]
    # 데이터를 learn 함수의 매개변수로 전달하여 학습
    learn(label, data=train_data)

    return jsonify({"message": "Learning completed"})



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