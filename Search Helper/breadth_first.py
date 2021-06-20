
from visual_helper import *


# Expand shallowest unexpanded node
def breadth_first_revamped(start, graph, goal):

    # Should store each list of children per height/level of the tree
    each_row = list()
    all_paths = list(start)
    new_paths = list()

    current_neighbors = sorted(graph[start])
    each_row.append(current_neighbors)

    while len(each_row) != 0:
        next_neighbors = set()
        new_paths = list()

        for path_node in all_paths:
            next_node = path_node[-1]
            current_neighbors = sorted(graph[next_node])

            if goal in current_neighbors:
                new_paths = path_node + goal
                break

            for node in current_neighbors:
                new_path = path_node + node
                new_paths.append(new_path)

            next_neighbors.update(current_neighbors)

        all_paths = new_paths
        each_row = list(next_neighbors)

    return get_path(list(new_paths))

# Expand shallowest unexpanded node
def breadth_first(start, graph, goal):
    
    # fringe is a FIFO Queue
    fringe = list(start)
    stack = list(start)
    # path = list()

    # Begin Loop
    while len(stack) != 0:
        next_node = stack.pop(0)
        # path.append(next_node)

        # Check for goal in the Queue
        if next_node == goal:
            break

        # Get the next lexicographic node children
        node_children = sorted(graph[next_node])
        fringe += ["|"] + stack + node_children

        # Check for goal in the Neighbors
        if goal in node_children:
            # path.append(goal)
            break

        stack += node_children

    # print(f"| The PATH: {get_path(path)}")
    return get_path(fringe)


#--------------------------------------------------------
if __name__ == "__main__":
    graph = {
        "A": ["G", "D", "B"],
        "B": ["F", "E"],
        "C": ["D", "H"],
        "D": ["G"],
        "E": [],
        "F": ["D", "C"],
        "G": [],
        "H": []
    }

    result = breadth_first_revamped("A", graph, "H")
    print("| PATH: ", result)
    result = breadth_first("A", graph, "H")
    print("| HELPER: ", result)