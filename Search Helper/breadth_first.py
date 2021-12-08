
from visual_helper import *
from test_graphs import *


# Expand shallowest unexpanded node
def breadth_first_path(start, graph, goal):

    # Should store each list of children per height/level of the tree
    each_row = list()
    all_paths = list(start)
    all_levels = start
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

        level = "".join( sorted(each_row) )
        all_levels += "|" + level

    print(f"| The PATH: {get_path(list(new_paths))}")
    return all_levels


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

    # result = breadth_first_path("A", graph, "H")
    result = breadth_first_path("A", tutorial2_graph, "G")
    print("| HELPER: ", get_path(result))