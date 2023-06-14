import base64
from io import BytesIO

from flask import Flask, request, jsonify

import path2
import path3
# from path2 import *
# from path3 import set_nodes as set_nodes_5


from whereami import *


# Set G on initial
path3.set_nodes()
path2.set_nodes()

app = Flask(__name__)

predicter = Predicter()


@app.route('/train', methods=['POST'])
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


@app.route('/path', methods=['POST'])
def find_path():
    data = request.get_json()
    start = data['start']
    end = data['end']
    if data['start'][0] == '4':
        if start == "4층 아르테크네":
            start == "7"
        if start == "418":
            start == "5"
        final_path, initial_pos, astar_path, intial_angle = path2.result_backend(
            start, end)
        path_image = path2.show_on_image(astar_path)

    elif data['start'][0] == '5':
        if start == "5층 아르테크네 앞 엘베":
            start = "8"
        final_path, initial_pos, astar_path, intial_angle = path2.result_backend(
            start, end)
        path_image = path3.show_on_image(astar_path)
    else:
        print("인식 할 수 없음")

    result_path = []

    for i in range(len(final_path)):
        if 'distance' in final_path[i]:
            distance = final_path[i]['distance']
        else:
            distance = 0

        if 'angle' in final_path[i]:
            angle = final_path[i]['angle']
            if angle > 180:
                angle = 270
            else:
                angle = 90
        else:
            angle = 0

        item = {'distance': distance, 'angle': angle}
        # print(item)
        result_path.append(item)

    if intial_angle < 0:
        intial_angle = intial_angle+360
    # for (i, item) in enumerate(result_path):
    #     # 예각은 그냥 90도로 표현, 둔각은 270도로 표현
    #     if item['angle'] > 180:
    #         item['angle'] = 270
    #     else:
    #         item['angle'] = 90
    response = {
        "start_direction": intial_angle,
        "path": result_path,
        "image": path_image,
    }

    return jsonify(response)


@app.route('/locations', methods=['GET'])
def get_locations():
    folder_path = ensure_whereami_path()
    location_list = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            location_list.append(file_name.replace('.txt', ''))

    response = {
        'locations': location_list
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
