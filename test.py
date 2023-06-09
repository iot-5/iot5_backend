data = [{'distance': 22}, {'angle': 90.0}, {'distance': 11}, {'distance': 13}, {
    'angle': 287.5255683737229}, {'distance': 25}, {'distance': 15}, {'distance': 5}]

merged_data = []
current_distance = None

for item in data:
    if 'distance' in item:
        distance_value = item['distance']
        if current_distance is None:
            current_distance = distance_value
        else:
            current_distance += distance_value
    else:
        if current_distance is not None:
            merged_data.append({'distance': current_distance})
            current_distance = None
        merged_data.append(item)

if current_distance is not None:
    merged_data.append({'distance': current_distance})

print(merged_data)
