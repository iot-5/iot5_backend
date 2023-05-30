from flask import Flask, request, jsonify
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
import pickle

app = Flask(__name__)

def train_manual_data(json_data, model_path=None):
    data = json.loads(json_data)
    label = data["name"]
    aps = data["data"]

    X = []
    y = []
    for ap in aps:
        X.append(ap)
        y.append(label)

    clf = RandomForestClassifier(n_estimators=100, class_weight="balanced")
    pipeline = make_pipeline(DictVectorizer(sparse=False), clf)
    pipeline.fit(X, y)

    if model_path is not None:
        with open(model_path, "wb") as f:
            pickle.dump(pipeline, f)

    return pipeline

def predict_manual_data(json_data, model_path):
    data = json.loads(json_data)
    aps = data["data"]

    with open(model_path, "rb") as f:
        pipeline = pickle.load(f)

    results = pipeline.predict(aps)
    return results

@app.route('/train', methods=['POST'])
def train():
    json_data = request.json
    model_path = "model.pkl"
    train_manual_data(json.dumps(json_data), model_path)
    return "Model trained successfully."

@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.json
    model_path = "model.pkl"
    predictions = predict_manual_data(json.dumps(json_data), model_path)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run()
