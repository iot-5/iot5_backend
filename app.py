from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


dataset = []
def calculate_euclidean_distance(pattern, rssi_values):
    distance = np.sqrt(np.sum((np.array(pattern) - np.array(rssi_values)) ** 2))
    return distance


@app.route('/addpoint', methods=['POST'])
def add_point():
    point_data = request.json
    name = point_data['name']
    data = [ap for ap in point_data['data']]
    dataset.append((name, data))
    return jsonify({'message': 'Point added successfully.'})

@app.route('/getpoint', methods=['POST'])
def get_point():
    rssi_values = [ap['rssi'] for ap in request.json['data']]
    matched_location = match_pattern(rssi_values)
    return jsonify({'location': matched_location})

def match_pattern(rssi_values):
    distances = []
    for data in dataset:
        pattern = [ap[ap_key] for ap in data[1] for ap_key in ap.keys()]
        distance = calculate_euclidean_distance(pattern, rssi_values)
        distances.append(distance)

    min_index = np.argmin(distances)
    matched_location = dataset[min_index][0]
    return matched_location

if __name__ == '__main__':
    app.run()