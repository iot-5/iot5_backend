import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

data = []

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

def calculate_distance(rssi1, rssi2):
    return abs(rssi1 - rssi2)

@app.route('/getpoint', methods=['POST'])
def get_point():
    json_data = request.get_json()

    mac_rssi_list = json_data['data']
    user_location = None
    min_distance = float('inf')

    for location in data:
        location_name = location[0]
        location_mac = location[1]
        location_rssi = int(location[2])

        for item in mac_rssi_list:
            mac = item['mac']
            rssi = item['rssi']

            if mac == location_mac:
                distance = calculate_distance(rssi, location_rssi)

                if distance < min_distance:
                    min_distance = distance
                    user_location = location_name

    return jsonify({'user_location': user_location})

if __name__ == '__main__':
    app.run()
