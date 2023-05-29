import json


def convert_dataset(dataset):
    converted_dataset = []

    for data in dataset:
        name = data['name']
        points = data['point']
        converted_points = []

        for point in points:
            mac = list(point.keys())[0]
            rssi = list(point.values())[0]
            converted_points.append({'mac': mac, 'rssi': rssi})

        converted_dataset.append((name, converted_points))

    return converted_dataset


# 주어진 dataset을 변환합니다.
converted_dataset = convert_dataset(dataset)

# 변환된 dataset을 JSON 형식으로 출력합니다.
converted_json = json.dumps(converted_dataset)
print(converted_json)
