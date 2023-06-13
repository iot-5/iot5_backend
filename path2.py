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

    return angle_deg, left


def draw_path_on_image(image_array, path):
    path_image = Image.fromarray(image_array)

    draw = ImageDraw.Draw(path_image)

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        draw.line((y1, x1, y2, x2), fill=(255, 0, 0), width=3)

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
        G.add_edge(node1, 1, weight=ueclidian_distance(x1, y1, 900, 1855))
        G.add_edge(node1, 3, weight=ueclidian_distance(x1, y1, 900, 1635))
        G.add_edge(node1, 5, weight=ueclidian_distance(x1, y1, 900, 735))
        G.add_edge(node1, 7, weight=ueclidian_distance(x1, y1, 900, 200))


def add_edges_from_top_line(G, top_line_nodes):
    for i in range(len(top_line_nodes) - 1):
        node1 = top_line_nodes[i]
        node2 = top_line_nodes[i + 1]
        x1, y1 = G.nodes[node1]['pos']
        x2, y2 = G.nodes[node2]['pos']
        weight = ueclidian_distance(x1, y1, x2, y2)
        G.add_edge(node1, node2, weight=weight)
        G.add_edge(node1, 2, weight=ueclidian_distance(x1, y1, 370, 1855))
        G.add_edge(node1, 4, weight=ueclidian_distance(x1, y1, 430, 1635))
        G.add_edge(node1, 6, weight=ueclidian_distance(x1, y1, 680, 735))
        G.add_edge(node1, 8, weight=ueclidian_distance(x1, y1, 830, 200))


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
    with open('rooms.json', 'r') as f:
        data = json.load(f)

    G.add_node(1, pos=(900, 1855))
    G.add_node(2, pos=(370, 1855))
    G.add_node(3, pos=(900, 1635))
    G.add_node(4, pos=(430, 1635))
    G.add_node(5, pos=(900, 735))
    G.add_node(6, pos=(680, 735))
    G.add_node(7, pos=(900, 200))
    G.add_node(8, pos=(830, 200))

    # 엘베 근처노드
    G.add_node(9, pos=(843, 710))  # 5,6라인
    G.add_node(10, pos=(773, 710))  # 5,6라인
    G.add_node(11, pos=(800, 1635))  # 3,4라인
    G.add_node(12, pos=(800, 1855))  # 1,2라인

    # 엘베노드
    G.add_node(101, pos=(834, 155))  # 1번엘베 8번노드연결
    G.add_node(102, pos=(845, 710))  # 2번엘베 9번노드연결
    G.add_node(103, pos=(776, 710))  # 3번엘베 10번노드연결
    G.add_node(104, pos=(801, 1696))  # 4번엘베 11번노드연결
    G.add_node(105, pos=(800, 1775))  # 5번엘베 12번노드연결

    G.add_edge(1, 2, weight=ueclidian_distance(900, 1855, 370, 1855))
    G.add_edge(3, 4, weight=ueclidian_distance(900, 1635, 430, 1635))
    G.add_edge(5, 6, weight=ueclidian_distance(900, 735, 680, 735))
    G.add_edge(7, 8, weight=ueclidian_distance(900, 200, 830, 200))
    G.add_edge(1, 3, weight=ueclidian_distance(900, 1855, 900, 1635))
    G.add_edge(3, 5, weight=ueclidian_distance(900, 1635, 900, 735))
    G.add_edge(5, 7, weight=ueclidian_distance(900, 735, 900, 200))
    G.add_edge(2, 4, weight=ueclidian_distance(370, 1855, 430, 1635))
    G.add_edge(4, 6, weight=ueclidian_distance(430, 1635, 680, 735))
    G.add_edge(6, 8, weight=ueclidian_distance(680, 735, 830, 200))

    # 엘베노드 연결
    G.add_edge(5, 9, weight=ueclidian_distance(900, 735, 843, 735))
    G.add_edge(6, 9, weight=ueclidian_distance(680, 735, 843, 735))
    G.add_edge(5, 10, weight=ueclidian_distance(900, 735, 773, 735))
    G.add_edge(6, 10, weight=ueclidian_distance(680, 735, 773, 735))
    G.add_edge(3, 11, weight=ueclidian_distance(900, 1635, 790, 1635))
    G.add_edge(4, 11, weight=ueclidian_distance(430, 1635, 790, 1635))
    G.add_edge(1, 12, weight=ueclidian_distance(900, 1855, 790, 1855))
    G.add_edge(2, 12, weight=ueclidian_distance(370, 1855, 790, 1855))

    G.add_edge(101, 8, weight=ueclidian_distance(834, 155, 830, 200))
    G.add_edge(102, 9, weight=ueclidian_distance(845, 708, 843, 735))
    G.add_edge(103, 10, weight=ueclidian_distance(776, 712, 773, 735))
    G.add_edge(104, 11, weight=ueclidian_distance(801, 1696, 790, 1635))
    G.add_edge(105, 12, weight=ueclidian_distance(800, 1775, 790, 1855))
    G.add_edge(102, 103, weight=ueclidian_distance(845, 708, 776, 712))
    G.add_edge(104, 105, weight=ueclidian_distance(801, 1696, 800, 1775))
    # Add nodes to the graph
    for room in data['rooms']:
        room_id = room['name']
        x = room['y']
        y = room['x']
        G.add_node(room_id, pos=(x, y))

    # Add edges based on the bottom line and top line
    bottom_line_nodes = [room['name']
                         for room in data['rooms'] if room.get('bottom', 0) == 0]
    top_line_nodes = [room['name']
                      for room in data['rooms'] if room.get('bottom', 0) == 1]
    elevator_nodes = [room['name']
                      for room in data['rooms'] if room.get('bottom', 2) == 1]
    add_edges_from_bottom_line(G, bottom_line_nodes)
    add_edges_from_top_line(G, top_line_nodes)

    # add edge in reverse direction
    for node1, node2 in G.edges():
        G.add_edge(node2, node1, weight=G[node1][node2][0]['weight'])

    # show all edges in the graph
    for node1, node2 in G.edges():
        print(node1, node2, G[node1][node2][0]['weight'])


def show_on_image(astar_path):
    # print(astar_path)
    path_line = []
    for i in range(len(astar_path)):
        path_line.append(G.nodes[astar_path[i]]['pos'])
    image_path = 'jj.png'
    image = Image.open(image_path).convert('RGB')
    image_array = np.array(image)
    path_image = draw_path_on_image(image_array, path_line)
    path_image.show()


# rotatation = [{"left": 90}, {"right": 90}, {"left": 164}, {"right": 164}]
# add rotation to the astar path


def result(start, end):
    set_nodes()
    real_world_scale = 0.04796469368
    initial_way_elevator = 0
    astar_path = nx.astar_path(G, start, end)
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

    show_on_image(astar_path)
    # print(final_path)
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
    print(merged_data)
    print(initial_way_elevator)
    return merged_data, initial_way_elevator

def result_cli(start, end):
    set_nodes()
    real_world_scale = 0.04796469368
    initial_way_elevator = 0
    astar_path = nx.astar_path(G, start, end)
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
    return merged_data, initial_way_elevator


if __name__ == "__main__":
    start = (input("Enter start room: "))
    end = (input("Enter end room: "))
    final_path, initial_pos = result(start, end)
    if initial_pos == 0:
        start_direct = "left"
    elif initial_pos == 1:
        start_direct = "right"
    else:
        start_direct = "None-개발중"
    print(start_direct)
    print(final_path)
