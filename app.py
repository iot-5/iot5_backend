import pickle

from flask import Flask, request, jsonify
from whereami import aps_to_dict, get_model, sample, get_external_sample, get_train_data, train_model

app = Flask(__name__)

model = None


def load_model():
    global model
    model = get_model("model.pkl")  # 모델 불러오기


@app.route('/predict', methods=['POST'])
def predict_location():
    load_model()  # 모델 로드
    data = request.get_json()
    wifi_samples = data['data']

    result = model.predict(aps_to_dict(wifi_samples))  # 예측

    return jsonify({'location': result[0]})


@app.route('/train', methods=['POST'])
def train_location():
    data = request.get_json()
    name = data['name']
    train_data = data['data']

    X, y = get_train_data()
    X.extend(train_data)
    y.extend([name] * len(train_data))

    train_model()

    return jsonify({'message': 'Training complete.'})


if __name__ == "__main__":
    load_model()  # 모델 로드
    app.run(host='0.0.0.0', port=5000)
