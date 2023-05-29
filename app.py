from flask import Flask, request, jsonify
import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# 데이터 로드
def load_data():
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data


# 데이터 추가 엔드포인트
@app.route('/addpoint/', methods=['POST'])
def add_point():
    point_data = request.get_json()
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for entry in point_data['data']:
            writer.writerow([point_data['name'], entry['mac'], entry['rssi']])
    return jsonify({'message': 'Data added successfully.'})

@app.route('/getpoint/', methods=['POST'])
def get_point():
    data = request.get_json()['data']
    loaded_data = load_data()
    predicted_names = []
    for entry in data:
        mac = entry['mac']
        rssi = entry['rssi']
        matched_points = [point for point in loaded_data if point[1] == mac]
        if matched_points:
            distances = [abs(float(point[2]) - float(rssi)) for point in matched_points]
            min_distance = min(distances)
            closest_points = [point for point, distance in zip(matched_points, distances) if distance == min_distance]
            closest_names = [point[0] for point in closest_points]
            predicted_name = max(set(closest_names), key=closest_names.count)
            predicted_names.append(predicted_name)
    return jsonify({'names': predicted_names})



if __name__ == '__main__':
    app.run()
