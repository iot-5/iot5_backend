from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


dataset = [
    ('p3', [{'mac': '91:9f:33:5c:23:09', 'rssi': 30}, {'mac': '95:1f:33:ac:35:3a', 'rssi': 50}, {'mac': '96:7f:23:55:29:87', 'rssi': 70}]),
    ('p1', [{'mac': '91:9f:33:5c:23:02', 'rssi': 20}, {'mac': '95:1f:33:ac:35:32', 'rssi': 70}, {'mac': '96:7f:23:55:29:82', 'rssi': 20}]),
    ('p2', [{'mac': '91:9f:33:5c:23:02', 'rssi': 40}, {'mac': '95:1f:33:ac:35:32', 'rssi': 80}, {'mac': '96:7f:23:55:29:82', 'rssi': 50}]),
    ('p4', [{'mac': '91:9f:33:5c:23:11', 'rssi': 40}, {'mac': '95:1f:33:ac:35:11', 'rssi': 80}, {'mac': '96:7f:23:55:29:11', 'rssi': 50}, {'mac': '91:9f:33:5c:23:02', 'rssi': 20}]),
]
def calculate_euclidean_distance(pattern, rssi_values):
    distance = np.sqrt(np.sum((np.array(pattern) - np.array(rssi_values)) ** 2))
    return distance


@app.route('/addpoint', methods=['POST'])
def add_point():
    point_data = request.json
    name = point_data['name']
    data = [{'mac': ap['mac'], 'rssi': ap['rssi']} for ap in point_data['data']]
    dataset.append((name, data))
    print(dataset)
    return jsonify({'message': 'Point added successfully.'})


@app.route('/getpoint', methods=['POST'])
def get_point():
    rssi_values = [ap['rssi'] for ap in request.json['data']]
    matched_location = match_pattern(rssi_values)
    return jsonify({'location': matched_location})



def match_pattern(rssi_values):
    distances = []
    for data in dataset:
        print(data)
        dataset_ap_values = [ap['rssi'] for ap in data[1]]
        min_length = min(len(rssi_values), len(dataset_ap_values))
        distance = calculate_euclidean_distance(dataset_ap_values[:min_length], rssi_values[:min_length])
        distances.append(distance)

    min_index = np.argmin(distances)
    matched_location = dataset[min_index][0]
    return matched_location

if __name__ == '__main__':
    app.run()