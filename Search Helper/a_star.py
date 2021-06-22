

from visual_helper import *
from uniform_cost import *


# It's more of a Dijkstra to me
def a_star(start, graph, node_price, goal):

    visited = set()
    fringe = list()
    fringe.append( [(start, 0)] )
    path = start
    path_expanded = start
    queue = list()
    total = 0

    next_node = (start, 0, 0, path)
    print()

    while True:
        node = next_node[0]
        weight = next_node[1]
        total += weight
        new_path = next_node[3]

        # Check for goal
        if node == goal:
            path = new_path
            break

        # Get the neighbors
        node_neighbors = graph[node]
        
        # Adds the node price to the node travel amount/cost
        temp_neighbors = list()
        for ele in node_neighbors:
            key = ele[0]
            key_value = ele[1]
            heuristic = node_price[key]
            new_value = (key_value + weight) + heuristic

            new_node = (key, new_value, key_value+weight, new_path+key)
            temp_neighbors.append(new_node)

        # Remove previously visited nodes
        temp_neighbors = remove_nodes(visited, temp_neighbors)

        # Add to the queue
        queue += temp_neighbors

        # Only want the node and overall value to be printed
        level = list()
        for ele in queue:
            fringe_node = (ele[0], ele[1])
            level.append(fringe_node)
        fringe.append(reorder(level)) # Add each node to the current level or queue

        # Get the smallest according to (path + heuristic) value
        next_node = get_smallest(queue)
        key = next_node[0]

        path_expanded += key
        print(f"| Smallest = ({key}, {next_node[2]})")
        
        # Pop the smallest, in this case remove it
        queue.remove(next_node)

        visited.add(node) # Mark it as a visited node
        next_node = (key, next_node[2], next_node[1], next_node[3]) # Update next node to smallest

    print(f"\n| The PATH: {get_path(path)}")
    print(f"| Nodes Expanded: {get_path(path_expanded)}")
    return fringe

#--------------------------------------------------------
if __name__ == "__main__":

    graph = {
        "A": [("Z", 75), ("T", 118), ("S", 140)],
        "B": [("P", 101), ("F", 211), ("G", 90), ("U", 85)],
        "C": [("D", 120), ("R", 146), ("P", 138)],
        "D": [("M", 75), ("C", 120)],
        "E": [("H", 86)],
        "F": [("S", 99), ("B", 211)],
        "G": [("B", 90)],
        "H": [("U", 98), ("E", 86)],
        "I": [("V", 92)],
        "J": [], # Empty -
        "K": [], # Empty -
        "L": [("M", 70), ("T", 111)],
        "M": [("D", 75), ("L", 70)],
        "N": [("I", 87)],
        "O": [("Z", 71), ("S", 151)],
        "P": [("R", 97), ("C", 138), ("B", 101)],
        "Q": [], # Empty -
        "R": [("S", 80), ("C", 148), ("P", 97)], # C-146?
        "S": [("O", 151), ("A", 140), ("R", 80), ("F", 99)],
        "T": [("A", 118), ("L", 111)],
        "U": [("B", 85), ("H", 98), ("V", 142)],
        "V": [("I", 92), ("U", 142)],
        "W": [], # Empty -
        "X": [], # Empty -
        "Y": [], # Empty -
        "Z": [("O", 71), ("A", 75)]
    }

    node_price = {
        "A": 366,
        "B": 0,
        "C": 160,
        "D": 242,
        "E": 161,
        "F": 176,
        "G": 77,
        "H": 151,
        "I": 226,
        "L": 244,
        "M": 241,
        "N": 234,
        "O": 380,
        "P": 100,
        "R": 193,
        "S": 253,
        "T": 329,
        "U": 80,
        "V": 199,
        "Z": 374
    }

    
    result = a_star("A", graph, node_price, "B")
    print()
    print(f"| The FRINGE: ")
    for ele in result:
        print(f"|  {ele}")