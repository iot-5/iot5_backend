import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import json
import math

G = nx.MultiDiGraph()


def calculate_angle(x1, y1, x2, y2, x3, y3):
    # Calculate the vectors for the two lines
    vector1 = (x2 - x1, y2 - y1)
    vector2 = (x3 - x2, y3 - y2)
    left = False
    # print(vector1[0]*vector2[0] + vector1[1]*vector2[1])
    # Calculate the dot product of the two vectors
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    if dot_product < 0:
        left = True
    if dot_product == 0:
        if vector1[0] == 0:
            if vector2[0] == 0:
                left = True
            else:
                if vector2[0] > 0:
                    left = False
                else:
                    left = True
        else:
            if vector1[0] > 0:
                left = True
            else:
                left = False
        # Calculate the magnitudes of the vectors
    magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
    magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

    # Calculate the cosine of the angle using the dot product and magnitudes
    cosine_angle = dot_product / (magnitude1 * magnitude2)

    # Calculate the angle in radians
    angle_rad = math.acos(cosine_angle)

    # Convert the angle to degrees
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

    add_edges_from_bottom_line(G, bottom_line_nodes)
    add_edges_from_top_line(G, top_line_nodes)

    # add edge in reverse direction
    for node1, node2 in G.edges():
        G.add_edge(node2, node1, weight=G[node1][node2][0]['weight'])


def show_on_image(astar_path):
    # print(astar_path)
    path_line = []
    for i in range(len(astar_path)):
        path_line.append(G.nodes[astar_path[i]]['pos'])
    image_path = 'jj.jpg'
    image = Image.open(image_path).convert('RGB')
    image_array = np.array(image)
    path_image = draw_path_on_image(image_array, path_line)
    path_image.show()


# rotatation = [{"left": 90}, {"right": 90}, {"left": 164}, {"right": 164}]
# add rotation to the astar path

def result(start, end):

    set_nodes()
    real_world_scale = 0.04796469368

    astar_path = nx.astar_path(G, start, end)
    if (len(astar_path) < 3):
        x1, y1 = G.nodes[astar_path[0]]['pos']
        x2, y2 = G.nodes[astar_path[1]]['pos']
        distance = ueclidian_distance(x1, y1, x2, y2)
        print(round(distance*real_world_scale))
    else:
        for i in range(len(astar_path) - 2):
            x1, y1 = G.nodes[astar_path[i]]['pos']
            x2, y2 = G.nodes[astar_path[i + 1]]['pos']
            x3, y3 = G.nodes[astar_path[i + 2]]['pos']
            distance1 = ueclidian_distance(x1, y1, x2, y2)
            angle, left = calculate_angle(x1, y1, x2, y2, x3, y3)
            print(round(distance1*real_world_scale))
            if angle < 8:
                continue
            if left:
                print(angle, "left")
            else:
                print(angle, "right")

            distance2 = ueclidian_distance(x2, y2, x3, y3)
        # print(distance2)

    show_on_image(astar_path)


if __name__ == "__main__":
    start = int(input("Enter start room: "))
    end = int(input("Enter end room: "))
    result(start, end)
