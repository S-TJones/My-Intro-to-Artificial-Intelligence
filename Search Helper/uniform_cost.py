
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
def remove_nodes(keys, queue):

    new_queue = list()

    if len(keys) == 0:
        return new_queue

    for node in queue:
        if node[0] not in keys:
            new_queue.append(node)

    return new_queue


def reform_output(path):

    new_list = list()
    prev = ""

    for ele in path:
        if not ele.isalpha():
            ele = prev + ele
            new_list = new_list[:-1]

        new_list.append(ele)
        prev = ele

    return new_list


def uniform_cost(start, graph, target):

    if type(target) != type([]):
        target = [target]

    def path_traveller(start, graph, path, total, all_paths=[]):

        if start in target:
            all_paths.append((path, total))
            return 

        # Get current node children
        node_children = graph[start]

        for node in node_children:
            node_key = node[0]
            new_path = path + node_key
            new_total = total + node[1]
            path_traveller(node_key, graph, new_path, new_total, all_paths)

        return all_paths

    paths = list()
    all_paths = path_traveller(start, graph, start, 0, paths)
    
    cheapest = get_smallest(all_paths)
    return cheapest

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
        "S": [("A", 1), ("B", 4)],
        "A": [("C", 3), ("D", 2)],
        "B": [("G", 5)],
        "C": [("E", 5)],
        "D": [("F", 0), ("G", 3)],
        "E": [("G", 5)],
        "F": [],
        "G": []
    }

    graph3 = {
        "S": [("D", 6), ("B1", 9), ("A", 5)],
        "A": [("G1", 9), ("B2", 3)],
        "B1": [],
        "B2": [("C2", 3)],
        "C": [("F", 7), ("G2", 5)],
        "C2": [],
        "D": [("E", 2), ("C", 2)],
        "E": [("G3", 7)],
        "F": [],
        "G1": [],
        "G2": [],
        "G3": []
    }

    # cheapest_path, cost = uniform_cost("A", graph, "G")
    # cheapest_path, cost = uniform_cost("S", graph2, "G")
    cheapest_path, cost = uniform_cost("S", graph3, ["G1", "G2", "G3"])

    print()
    result = get_path( reform_output(cheapest_path) )
    print(f"| The PATH: {result}")
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