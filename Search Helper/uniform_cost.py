
from visual_helper import *


# Sorts the queue according to priority
def reorder(queue):

    smallest_num = float("inf")
    smallest_node = None

    length = len(queue)
    current_index = 0

    new_queue = list()

    while current_index < length:
        
        for node in queue: # TODO: Replace with get_smallest
            number = node[1]

            if number < smallest_num:
                smallest_num = number
                smallest_node = node

        new_queue.append(smallest_node)
        smallest_num = float("inf")
        current_index += 1
        queue.remove(smallest_node)

    return new_queue


# Inserts a node according to it's priority
def insert_into(queue, element):

    # This function assumes the queue is already sorted
    number = element[1]
    new_location = -1

    for x in range(len(queue)):
        node = queue[x]
        node_num = node[1]

        if number < node_num:
            new_location = x
            break

    # Check to see if the index was updated
    if new_location == -1:
        queue.append(element)
    else:
        queue.insert(new_location, element)

    return queue


# Gets the node with the smallest weight
def get_smallest(queue):

    smallest_num = float("inf")
    smallest_node = None

    for node in queue:
        number = node[1]

        if number < smallest_num:
            smallest_num = number
            smallest_node = node

    return smallest_node


# Adds the weight to all nodes in the queue
def add_all(number, queue):
    
    new_queue = list()

    for node in queue:
        node_letter = node[0]
        node_num = node[1] + number

        new_tuple = (node_letter, node_num)
        new_queue.append(new_tuple)

    return new_queue


# Removes all nodes with the matching key
def remove_nodes(key, queue):

    new_queue = list()

    for node in queue:
        if node[0] != key:
            new_queue.append(node)

    return new_queue


def uniform_cost(start, graph):
    
    # fringe is a Priority-Queue
    visited = set()
    path = list()
    queue = list()
    length = graph
    total = 0

    next_node = (start, 0)
    
    while True:
        node = next_node[0]
        weight = next_node[1]
        total += weight

        path.append(f"{node} - {weight}")

        node_neighbors = graph[node]

        for key in visited:
            node_neighbors = remove_nodes(key, node_neighbors)
        
        # If there are no new nodes, then we've visited them all
        if node_neighbors == []:
            break

        node_neighbors = add_all(weight, node_neighbors)
        queue += node_neighbors
        
        next_node = get_smallest(queue)

        queue.remove(next_node)
        visited.add(node)

    return path, total


#--------------------------------------------------------
if __name__ == "__main__":
    graph = {
        "A": [("G", 95), ("D", 80), ("B", 20)],
        "B": [("F", 10), ("E", 50)],
        "C": [("D", 50), ("H", 20)],
        "D": [("G", 10)],
        "E": [],
        "F": [("D", 40), ("C", 10)],
        "G": [],
        "H": []
    }

    graph2 = {
        "V0": [("V1", 9), ("V4", 5), ("V3", 4)],
        "V1": [("V0", 9), ("V4", 12), ("V3", 4), ("V2", 1)],
        "V2": [("V1", 1), ("V4", 8), ("V3", 2)],
        "V3": [("V2", 2), ("V0", 4), ("V1", 4)],
        "V4": [("V0", 5), ("V1", 12), ("V2", 8)]
    }

    graph3 = {
        "A": [("B", 16), ("C", 3), ("H", 2), ("F", 16)],
        "B": [("A", 16), ("F", 15), ("H", 19), ("C", 8)],
        "C": [("B", 8), ("A", 3), ("G", 13), ("E", 9), ("H", 15)],
        "D": [("E", 11), ("G", 16)],
        "E": [("C", 9), ("G", 6), ("H", 5), ("D", 11)],
        "F": [("A", 16), ("B", 15), ("H", 14)],
        "G": [("C", 13), ("D", 16), ("E", 6), ("H", 10)],
        "H": [("G", 10), ("C", 15), ("B", 19), ("A", 2), ("F", 14), ("E", 5)]
    }

    # cheapest_path, cost = uniform_cost("A", graph)
    # cheapest_path, cost = uniform_cost("V0", graph2)
    cheapest_path, cost = uniform_cost("A", graph3)

    result = "\n| ".join(cheapest_path)
    print(f"| The PATH: \n| {result}")
    print(f"| The COST: {cost}")

    # Testing Helper functions ------------------------
    # print(reorder(graph["A"]))

    # node_b = graph["B"]
    # print(insert_into(node_b, ("Z", 25)))
    # print(insert_into(node_b, ("Z", 50)))
    # print(insert_into(node_b, ("Z", 5)))
    # print(insert_into(node_b, ("Z", 60)))

    # print(add_all(0, graph2["V1"]))
    # print(add_all(10, graph2["V1"]))

    # print(get_smallest(graph2["V1"]))
    # print(get_smallest(graph2["V0"]))
    # print(get_smallest(graph2["V3"]))