
from visual_helper import *


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

    result = breadth_first("A", graph, "H")
    print("| HELPER: ", result)