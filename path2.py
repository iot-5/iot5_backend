import base64
import os
import platform
import time

import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import json
import math

G = nx.MultiDiGraph()


def calculate_rotation(x1, y1, x2, y2, x3, y3):
    vector1 = (x2 - x1, y2 - y1)
    vector2 = (x3 - x2, y3 - y2)

    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    if cross_product > 0:
        rotation = 'left'
    elif cross_product < 0:
        rotation = 'right'
    else:
        rotation = 'straight'

    return rotation


def calculate_angle(x1, y1, x2, y2, x3, y3):
    rotation = calculate_rotation(x1, y1, x2, y2, x3, y3)
    left = (rotation == 'left')
    angle_deg = None  # angle_deg 변수 초기화

    if rotation != 'straight':
        vector1 = (x2 - x1, y2 - y1)
        vector2 = (x3 - x2, y3 - y2)

        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

        magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
        magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

        cosine_angle = dot_product / (magnitude1 * magnitude2)

        angle_rad = math.acos(cosine_angle)

        angle_deg = math.degrees(angle_rad)

    else:
        angle_deg = 0

        if (x2-x1) * (x2-x3) < 0:
            left = True
    return angle_deg, left


def draw_path_on_image(image_array, path):
    path_image = Image.fromarray(image_array)
    draw = ImageDraw.Draw(path_image)

    # Draw the path as a thick red line
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        draw.line((y1, x1, y2, x2), fill=(255, 0, 0), width=10)

    # Draw blue circles at the start and end points
    start_x, start_y = path[0]
    end_x, end_y = path[-1]
    radius = 10
    draw.ellipse((start_y - radius, start_x - radius, start_y +
                 radius, start_x + radius), fill=(40, 152, 255))
    # draw.ellipse((end_y - radius, end_x - radius, end_y +
    #              radius, end_x + radius), fill=(40, 152, 255))

    # Load the marker image
    marker_image_path = "marker2.png"
    marker_image = Image.open(marker_image_path).convert("RGBA")

    marker_width, marker_height = marker_image.size
    new_width = int(marker_width * 0.5)
    new_height = int(marker_height * 0.5)
    marker_image = marker_image.resize((new_width, new_height))

    # Calculate the marker position
    dest_x, dest_y = path[-1]
    marker_x = int(dest_x - new_width-10)
    marker_y = int(dest_y - new_height/3)
    # Paste the marker image onto the path image
    path_image.paste(marker_image, (marker_y, marker_x), marker_image)

    # Draw destination name below the marker
    # Choose the desired font and size
    # font = ImageFont.truetype("arial.ttf", 16)
    # text_width, text_height = draw.textsize(destination_name)
    # text_x = dest_x + radius - text_width // 2
    # text_y = dest_y + radius + 5
    # draw.text((text_y, text_x), destination_name, fill=(0, 0, 0))

    return path_image


def ueclidian_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def add_edges_from_bottom_line(G, bottom_line_nodes):
    for i in range(len(bottom_line_nodes) - 1):
        node1 = bottom_line_nodes[i]
        node2 = bottom_line_nodes[i + 1]
        x1, y1 = G.nodes[node1]['pos']
        x2, y2 = G.nodes[node2]['pos']
        weight = ueclidian_distance(x1, y1, x2, y2)
        G.add_edge(node1, node2, weight=weight)
        G.add_edge(node1, "1", weight=ueclidian_distance(x1, y1, 909, 1882.5))
        G.add_edge(node1, "3", weight=ueclidian_distance(x1, y1, 909, 1633.25))
        G.add_edge(node1, "5", weight=ueclidian_distance(x1, y1, 909, 739.5))
        G.add_edge(node1, "7", weight=ueclidian_distance(x1, y1, 909, 181))


def add_edges_from_top_line(G, top_line_nodes):
    for i in range(len(top_line_nodes) - 1):
        node1 = top_line_nodes[i]
        node2 = top_line_nodes[i + 1]
        x1, y1 = G.nodes[node1]['pos']
        x2, y2 = G.nodes[node2]['pos']
        weight = ueclidian_distance(x1, y1, x2, y2)
        G.add_edge(node1, node2, weight=weight)
        G.add_edge(node1, "2", weight=ueclidian_distance(x1, y1, 338, 1882.5))
        G.add_edge(node1, "4", weight=ueclidian_distance(
            x1, y1, 409.3, 1633.25))
        G.add_edge(node1, "6", weight=ueclidian_distance(
            x1, y1, 667.29, 739.5))
        G.add_edge(node1, "8", weight=ueclidian_distance(x1, y1, 828.5, 181))


def add_edges_from_right_line(G, right_nodes):
    for i in range(len(right_nodes) - 1):
        node1 = right_nodes[i]
        node2 = right_nodes[i + 1]
        x1, y1 = G.nodes[node1]['pos']
        x2, y2 = G.nodes[node2]['pos']
        weight = ueclidian_distance(x1, y1, x2, y2)
        G.add_edge(node1, node2, weight=weight)
        # 1번, 2번 노드 연결
        G.add_edge(node1, "1", weight=ueclidian_distance(x1, y1, 909, 1882.5))
        G.add_edge(node1, "2", weight=ueclidian_distance(x1, y1, 338, 1882.5))


def calculate_third_side_length(side1, side2, angle):
    # Convert the angle to radians
    angle_rad = math.radians(angle)

    # Calculate the square of the third side length using the law of cosines
    side3_squared = side1**2 + side2**2 - 2 * \
        side1 * side2 * math.cos(angle_rad)

    # Take the square root to get the actual length of the third side
    side3 = math.sqrt(side3_squared)

    return side3


def set_nodes():
    check_point = [1, 2, 3, 4, 5, 6, 7, 8]
    # Read JSON file
    with open('rooms_4.json', 'r') as f:
        data = json.load(f)

    G.add_node("1", pos=(909, 1882.5))
    G.add_node("2", pos=(338, 1882.5))
    G.add_node("3", pos=(909, 1633.25))
    G.add_node("4", pos=(409.3, 1633.25))
    G.add_node("5", pos=(909, 739.5))
    G.add_node("6", pos=(667.29, 739.5))
    G.add_node("7", pos=(909, 181))
    G.add_node("8", pos=(828.5, 181))

    G.add_edge("1", "2", weight=ueclidian_distance(909, 1882.5, 338, 1882.5))
    G.add_edge("3", "4", weight=ueclidian_distance(
        909, 1633.25, 409.3, 1633.25))
    G.add_edge("5", "6", weight=ueclidian_distance(909, 739.5, 667.29, 739.5))
    G.add_edge("7", "8", weight=ueclidian_distance(909, 181, 828.5, 181))

    G.add_edge("1", "3", weight=ueclidian_distance(909, 1882.5, 909, 1633.25))
    G.add_edge("3", "5", weight=ueclidian_distance(909, 1633.25, 909, 739.5))
    G.add_edge("5", "7", weight=ueclidian_distance(909, 739.5, 909, 181))
    G.add_edge("2", "4", weight=ueclidian_distance(
        338, 1882.5, 409.3, 1633.25))
    G.add_edge("4", "6", weight=ueclidian_distance(
        409.3, 1633.25, 667.29, 739.5))
    G.add_edge("6", "8", weight=ueclidian_distance(667.29, 739.5, 828.5, 181))

    G.add_node("4층테라스", pos=(828.5, 794))
    G.add_node("테라스_1", pos=(828.5, 739.5))  # 5,6 라인

    G.add_edge("4층테라스", "테라스_1", weight=ueclidian_distance(
        828.5, 794, 828.5, 739.5))
    G.add_edge("테라스_1", "6", weight=ueclidian_distance(
        828.5, 739.5, 667.29, 739.5))
    G.add_edge("테라스_1", "5", weight=ueclidian_distance(
        828.5, 739.5, 909, 739.5))

    # 엘베 근처노드
    # G.add_node("9", pos=(835, 739.5))  # 5,6라인
    G.add_node("4층 테라스앞 엘베", pos=(790.69, 739.5))  # 5,6라인

    # G.add_edge("5", "9", weight=ueclidian_distance(909, 739.5, 835, 739.5))
    # G.add_edge("6", "9", weight=ueclidian_distance(667.29, 739.5, 835, 739.5))
    G.add_edge("5", "4층 테라스앞 엘베", weight=ueclidian_distance(
        909, 739.5, 790.69, 739.5))
    G.add_edge("6", "4층 테라스앞 엘베", weight=ueclidian_distance(
        667.29, 739.5, 790.69, 739.5))
    # G.add_edge("3", "11", weight=ueclidian_distance(
    #     909, 1633.25, 790.69, 1633.25))
    # G.add_edge("4", "11", weight=ueclidian_distance(
    #     409.3, 1633.25, 790.69, 1633.25))
    # G.add_edge("1", "12", weight=ueclidian_distance(
    #     909, 1882.5, 790.69, 1882.5))
    # G.add_edge("2", "12", weight=ueclidian_distance(
    #     338, 1882.5, 790.69, 1882.5))
    G.add_node("4층 게시판 엘베", pos=(790.69, 1731.25))
    G.add_node("게시판 앞 엘베_1", pos=(790.69, 1633.25))  # 3,4라인
    G.add_node("게시판 앞 엘베_2", pos=(790.69, 1882.5))  # 1,2라인

    G.add_edge("4층 게시판 엘베", "게시판 앞 엘베_1", weight=ueclidian_distance(
        1731.25, 790.69, 790.69, 1633.25))
    G.add_edge("4층 게시판 엘베", "게시판 앞 엘베_2", weight=ueclidian_distance(
        1731.25, 790.69, 790.69, 1882.5))

    G.add_edge("게시판 앞 엘베_1", "3", weight=ueclidian_distance(
        790.69, 1633.25, 909, 1633.25))
    G.add_edge("게시판 앞 엘베_1", "4", weight=ueclidian_distance(
        790.69, 1633.25, 409.3, 1633.25))
    G.add_edge("게시판 앞 엘베_2", "1", weight=ueclidian_distance(
        790.69, 1882.5, 909, 1882.5))
    G.add_edge("게시판 앞 엘베_2", "2", weight=ueclidian_distance(
        790.69, 1882.5, 338, 1882.5))

    # 엘베노드
    # G.add_node("101", pos=(828.5, 146.5))  # 1번엘베 8번노드연결
    # G.add_node("102", pos=(845, 691))  # 2번엘베 9번노드연결
    # G.add_node("103", pos=(790.69, 691))  # 3번엘베 10번노드연결
    # G.add_node("104", pos=(790.69, 1692.5))  # 4번엘베 11번노드연결
    # G.add_node("105", pos=(790.69, 1770))  # 5번엘베 12번노드연결

    # G.add_edge("8", "101", weight=ueclidian_distance(828.5, 181, 828.5, 146.5))
    # G.add_edge("9", "102", weight=ueclidian_distance(835, 739.5, 845, 691))
    # G.add_edge("10", "103", weight=ueclidian_distance(
    #     790.69, 739.5, 790.69, 691))
    # G.add_edge("11", "104", weight=ueclidian_distance(
    #     790.69, 1633.25, 790.69, 1692.5))
    # G.add_edge("12", 105, weight=ueclidian_distance(
    #     790.69, 1882.5, 790.69, 1770))
    # G.add_edge("102", "103", weight=ueclidian_distance(845, 691, 790.69, 691))
    # G.add_edge("104", "105", weight=ueclidian_distance(
    #     790.69, 1692.5, 790.69, 1770))

    # Add nodes to the graph
    for room in data['rooms']:
        room_id = room['name']
        x = room['y']
        y = room['x']
        G.add_node(room_id, pos=(x, y))

    # Add edges based on the bottom line and top line
    bottom_line_nodes = [room['name']
                         for room in data['rooms'] if room['bottom'] == 0]
    top_line_nodes = [room['name']
                      for room in data['rooms'] if room['bottom'] == 1]
    right_node = [room['name']
                  for room in data['rooms'] if room['bottom'] == 2]
    # for room in data['rooms']:
    #     print(room['bottom'])
    # print(right_node)
    add_edges_from_bottom_line(G, bottom_line_nodes)
    add_edges_from_top_line(G, top_line_nodes)
    add_edges_from_right_line(G, right_node)

    # add edge in reverse direction
    for node1, node2 in list(G.edges()):
        G.add_edge(node2, node1, weight=G[node1][node2][0]['weight'])

    # # show all edges in the graph
    # for node1, node2 in G.edges():
    #     print(node1, node2, G[node1][node2][0]['weight'])


def show_on_image(astar_path):
    # print(astar_path)
    path_line = []
    for i in range(len(astar_path)):
        path_line.append(G.nodes[astar_path[i]]['pos'])
    image_path = '4th.png'
    image = Image.open(image_path).convert('RGB')
    image_array = np.array(image)
    path_image = draw_path_on_image(image_array, path_line)

    if not platform.system() == 'Linux':
        path_image.show()

    # Save image with a unique filename
    filename = f'path_image_{int(time.time())}.png'
    path_image.save(filename)
    # Wait for the image to be saved
    while not os.path.exists(filename):
        time.sleep(0.1)

    # Encode the saved image to base64
    with open(filename, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Remove the temporary image file
    os.remove(filename)

    return encoded_image


# rotatation = [{"left": 90}, {"right": 90}, {"left": 164}, {"right": 164}]
# add rotation to the astar path


def result(start, end):
    set_nodes()
    # print(list(G.edges()))
    real_world_scale = 0.04796469368
    real_world_angle = 6.25
    initial_way_elevator = 0
    astar_path = nx.astar_path(G, start, end)

    initial_angle, left = calculate_angle(G.nodes[astar_path[0]]['pos'][0]-1, G.nodes[astar_path[0]]
                                          ['pos'][1], G.nodes[astar_path[0]]['pos'][0], G.nodes[astar_path[0]]['pos'][1], G.nodes[astar_path[1]]['pos'][0], G.nodes[astar_path[1]]['pos'][1])
    if initial_angle == 0:
        if left == 1:
            initial_angle = 180
        else:
            initial_angle = 0
    else:
        if left == 1:
            initial_angle = 180 - initial_angle
        else:
            initial_angle = initial_angle + 180
    print("initial angle: ", initial_angle)
    print(astar_path)
    distance = 0
    final_path = []
    if (G.nodes[astar_path[0]]['pos'][1] < G.nodes[astar_path[1]]['pos'][1]):
        initial_way_elevator = 1
    elif (G.nodes[astar_path[0]]['pos'][1] > G.nodes[astar_path[1]]['pos'][1]):
        initial_way_elevator = 0
    else:
        initial_way_elevator = 2

    if len(astar_path) < 3:
        x1, y1 = G.nodes[astar_path[0]]['pos']
        x2, y2 = G.nodes[astar_path[1]]['pos']
        distance = ueclidian_distance(x1, y1, x2, y2)
        final_path.append({'distance': round(distance * real_world_scale)})
    else:
        for i in range(len(astar_path) - 2):
            x1, y1 = G.nodes[astar_path[i]]['pos']
            x2, y2 = G.nodes[astar_path[i + 1]]['pos']
            x3, y3 = G.nodes[astar_path[i + 2]]['pos']

            angle_deg, left = calculate_angle(x1, y1, x2, y2, x3, y3)
            distance = ueclidian_distance(x1, y1, x2, y2)
            final_path.append({"distance": round(distance * real_world_scale)})

            if angle_deg is None:
                continue

            if left:
                # print(angle_deg, "left")
                final_path.append({"angle": angle_deg})
            else:
                # print(angle_deg, "right")
                final_path.append({"angle": 360-angle_deg})

            # print(distance2)
        last_room1 = astar_path[-2]
        last_room2 = astar_path[-1]
        final_path.append({'distance': round(ueclidian_distance(G.nodes[last_room1]['pos'][0], G.nodes[last_room1]['pos'][1],
                                                                G.nodes[last_room2]['pos'][0], G.nodes[last_room2]['pos'][1]) * real_world_scale)})

    show_on_image(astar_path)
    # print("ff: ", final_path)
    for i in range(len(final_path)):
        if 'angle' in final_path[i]:
            # print(i['angle'])
            if final_path[i]['angle'] < 10 or final_path[i]['angle'] > 350:
                final_path[i] = {"distance": round(calculate_third_side_length(
                    final_path[i-1]['distance'], final_path[i+1]['distance'], 180-final_path[i]['angle']))}
                final_path[i-1] = {'distance': 0}
                final_path[i+1] = {'distance': 0}
                i = i+1

    # delete {"distance": 0} in list, but don't touch "angle"
    print("ff", final_path)
    final_path = [i for i in final_path if i.get(
        'distance', 0) != 0 or i.get('angle', 0) != 0]
    merged_data = []

    current_distance = None

    for item in final_path:
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
    # print(merged_data)
    print(initial_way_elevator)
    return merged_data, initial_way_elevator


def result_backend(start, end):
    real_world_scale = 0.04796469368
    initial_way_elevator = 0
    real_world_angle = 6.25
    astar_path = nx.astar_path(G, start, end)
    distance = 0
    final_path = []
    if (G.nodes[astar_path[0]]['pos'][1] < G.nodes[astar_path[1]]['pos'][1]):
        initial_way_elevator = 1
    elif (G.nodes[astar_path[0]]['pos'][1] > G.nodes[astar_path[1]]['pos'][1]):
        initial_way_elevator = 0
    else:
        initial_way_elevator = 2

    initial_angle, left = calculate_angle(G.nodes[astar_path[0]]['pos'][0]-1, G.nodes[astar_path[0]]
                                          ['pos'][1], G.nodes[astar_path[0]]['pos'][0], G.nodes[astar_path[0]]['pos'][1], G.nodes[astar_path[1]]['pos'][0], G.nodes[astar_path[1]]['pos'][1])
    if initial_angle == 0:
        if left == 1:
            initial_angle = 180
        else:
            initial_angle = 0
    else:
        if left == 1:
            initial_angle = 180 - initial_angle
        else:
            initial_angle = initial_angle + 180

    if len(astar_path) < 3:
        x1, y1 = G.nodes[astar_path[0]]['pos']
        x2, y2 = G.nodes[astar_path[1]]['pos']
        distance = ueclidian_distance(x1, y1, x2, y2)
        final_path.append(round(distance * real_world_scale))
    else:
        for i in range(len(astar_path) - 2):
            x1, y1 = G.nodes[astar_path[i]]['pos']
            x2, y2 = G.nodes[astar_path[i + 1]]['pos']
            x3, y3 = G.nodes[astar_path[i + 2]]['pos']

            angle_deg, left = calculate_angle(x1, y1, x2, y2, x3, y3)
            distance = ueclidian_distance(x1, y1, x2, y2)
            final_path.append({"distance": round(distance * real_world_scale)})

            if angle_deg is None:
                continue

            if left:
                # print(angle_deg, "left")
                final_path.append({"angle": angle_deg})
            else:
                # print(angle_deg, "right")
                final_path.append({"angle": 360-angle_deg})

            # print(distance2)
        last_room1 = astar_path[-2]
        last_room2 = astar_path[-1]
        final_path.append({'distance': round(ueclidian_distance(G.nodes[last_room1]['pos'][0], G.nodes[last_room1]['pos'][1],
                                                                G.nodes[last_room2]['pos'][0], G.nodes[last_room2]['pos'][1]) * real_world_scale)})

    # print(final_path)
    for i in range(len(final_path)):
        if 'angle' in final_path[i]:
            # print(i['angle'])
            if final_path[i]['angle'] < 10:
                final_path[i] = {"distance": round(calculate_third_side_length(
                    final_path[i-1]['distance'], final_path[i+1]['distance'], 180-final_path[i]['angle']))}
                final_path[i-1] = {'distance': 0}
                final_path[i+1] = {'distance': 0}
                i = i+1

    # delete {"distance": 0} in list, but don't touch "angle"

    final_path = [i for i in final_path if i.get(
        'distance', 0) != 0 or i.get('angle', 0) != 0]
    merged_data = []

    current_distance = None

    for item in final_path:
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
    return merged_data, initial_way_elevator, astar_path, initial_angle + real_world_angle


if __name__ == "__main__":
    start = (input("Enter start room: "))
    end = (input("Enter end room: "))
    if start == "아르테크네":
        start = "7"
    final_path, initial_pos = result(start, end)

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
        print(item)
        result_path.append(item)

    print(result_path)
