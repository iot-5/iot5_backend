import pickle

from flask import Flask, request, jsonify

from whereami import train_manual_data, predict_manual_data

app = Flask(__name__)

@app.route("/train", methods=["POST"])
def train_location():
    try:
        req_data = request.get_json()
        name = req_data["name"]
        data = req_data["data"]

        labels = [name]
        train_data = [data]

        model_path = "model.pkl"  # 모델 파일 경로를 지정하거나 None으로 설정하여 저장하지 않음

        model = train_manual_data(train_data, labels, model_path)


        return jsonify({"message": "Training successful."})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/predict", methods=["POST"])
def predict_location():
    try:
        req_data = request.get_json()
        data = req_data["data"]

        model_path = "model.pkl"  # 모델 파일 경로를 지정합니다. 학습된 모델 파일의 경로여야 합니다.

        results = predict_manual_data(data, model_path)
        results_list = [arr.tolist() for arr in results]

        return jsonify({"results": results_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 400



if __name__ == "__main__":
    app.run()
