

from visual_helper import *
from uniform_cost import *
from test_graphs import *


# It's more of a Dijkstra to me
def a_star(start, graph, node_heuristics, goal):

    visited = set()
    fringe = list()
    fringe.append( [(start, 0)] )
    path = start
    path_expanded = start
    queue = list()
    total = 0

    next_node = (start, 0, 0, path)

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
            heuristic = node_heuristics[key]
            new_value = (key_value + weight) + heuristic

            new_node = (key, new_value, key_value+weight, new_path+key)
            temp_neighbors.append(new_node)

        # Remove previously visited nodes
        temp_neighbors = remove_nodes(visited, temp_neighbors)
        print(temp_neighbors)

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
        
        # Pop the smallest, in this case remove it
        queue.remove(next_node)

        visited.add(node) # Mark it as a visited node
        next_node = (key, next_node[2], next_node[1], next_node[3]) # Update next node to smallest

    print(f"\n| The PATH: {get_path(path)}")
    print(f"| Nodes Expanded: {get_path(path_expanded)}")
    return fringe

#--------------------------------------------------------
if __name__ == "__main__":

    result = a_star("A", tutorial3_graph, tutorial3_heuristics, "B")

    # Assignment Tests
    # result = a_star("A", graphT1, heurist_graphT1, "G") #Expects ['A', 'B', 'F', 'D', 'G']
    # result = a_star("A", graphT2, heurist_graphT2, "B") #Expects ['A', 'S', 'R', 'P', 'B']
    # result = a_star("T", graphT2, heurist_graphT2, "B") #Expects ['T', 'A', 'S', 'R', 'P', 'B']

    print()
    print(f"| The FRINGE: ")
    for ele in result:
        print(f"|  {ele}")