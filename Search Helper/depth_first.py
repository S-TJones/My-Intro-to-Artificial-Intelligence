
from visual_helper import *


# Depth First Traversal
def depth_first(start, graph, goal):
    
    # fringe is a stack
    fringe = list(start)
    stack = list(start)
    path = list()

    # Begin Loop
    while len(stack) != 0:
        next_node = stack.pop(0)
        path.append(next_node)

        # Check for goal in the Stack
        if next_node == goal:
            break

        # Get the next lexicographic node children
        node_children = sorted(graph[next_node])

        fringe += ["|"] + node_children + stack
        stack = node_children + stack

    print(f"| The PATH: {get_path(path)}")
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

    result = depth_first("A", graph, "G")
    print("| HELPER: ", result)