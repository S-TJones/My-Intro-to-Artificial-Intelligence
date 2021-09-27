
from visual_helper import *
from test_graphs import *

# Sorts the queue according to priority
def reorder(queue):

    smallest_num = float("inf")
    smallest_node = None

    length = len(queue)
    current_index = 0

    new_queue = list()

    while len(queue) != 0:
        
        smallest_node = get_smallest(queue)

        new_queue.append(smallest_node)
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
        return queue

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

    # Gets the Fringe
    def fringe_getter(start, graph):
        queue = [(start, 0)]

        print(f"\n| The FRINGE:\n| {queue}")

        while len(queue) != 0:
            next_node = queue.pop(0)
            key = next_node[0]
            weight = next_node[1]

            if key in target:
                break

            # This check is insurance for empty nodes not declared in the graph
            if start not in graph.keys():
                node_children = []
            else:
                node_children = graph[key]

            node_children = add_all(weight, node_children)
            # node_children = reorder(node_children)

            queue = reorder(queue + node_children)
            print(f"| {queue}")
        
    #-----------------------------------------------

    # Checks all possible paths and stores the paths that get to the target
    def path_traveller(start, graph, path, total):

        if start in target:
            all_paths.append((path, total))
            return 0

        # Get current node children
        if start not in graph.keys():
            node_children = []
        else:
            node_children = graph[start]

        # Remove visited nodes for bi-directional graphs
        node_children = remove_nodes(path, node_children)

        if node_children == []:
            return 0

        for node in node_children:
            node_key = node[0]
            new_path = path + node_key
            new_total = total + node[1]
            path_traveller(node_key, graph, new_path, new_total)

        #------------- End of Helper Function ---------------------------

    # Global list to store all paths
    all_paths = list()
    
    path_traveller(start, graph, start, 0)
    cheapest = get_smallest(all_paths)

    # Prints the fringe
    fringe_getter(start, graph)

    return cheapest

#--------------------------------------------------------
if __name__ == "__main__":
    final_exam = {
        "A": [('B', 8), ('F', 6)],
        "B": [('A', 10), ('D', 7), ('C', 5)],
        "C": [('B', 8), ('D', 7), ('E', 3)],
        "D": [('B', 8), ('C', 5), ('E', 3)],
        "E": [('C', 5), ('D', 7), ('I', 1), ('J', 0)],
        "F": [('A', 10), ('G', 5), ('H', 3)],
        "G": [('F', 6), ('I', 1)],
        "H": [('F', 6), ('I', 1)],
        "I": [('G', 5), ('H', 3), ('J', 0), ('E', 3)],
        "J": [('E', 3), ('I', 1)]
    }

    # My Tests
    # cheapest_path, cost = uniform_cost("A", midsem_graph, "G")
    # cheapest_path, cost = uniform_cost("A", final_exam, "J")
    # cheapest_path, cost = uniform_cost("S", graph2, "G")
    # cheapest_path, cost = uniform_cost("S", graph3, ["G1", "G2", "G3"])
    cheapest_path, cost = uniform_cost("A", tutorial2_graph, "G")

    # Assignment Tests
    # cheapest_path, cost = uniform_cost("F", graphT1, "G") #Expects ['F', 'D', 'G']
    # cheapest_path, cost = uniform_cost("T", graphT2, "B") #Expects ['T', 'A', 'S', 'R', 'P', 'B']
    # cheapest_path, cost = uniform_cost("O", graphT2, "B") #Expects ['O', 'S', 'R', 'P', 'B']
    # cheapest_path, cost = uniform_cost("D", graphT2, "B") #Expects ['D', 'C', 'P', 'B']

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