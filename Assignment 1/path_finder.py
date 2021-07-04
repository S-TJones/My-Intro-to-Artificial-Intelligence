
"""
    Name: Shemar Jones
    ID: 620117968
    Course Code: COMP3220
    Course Title: Principles of Artificial Intelligence

    Assignment #1
"""



class PriorityQueue:
    
    def __init__(self):
        self.queue = []

    # Gets the length of the Priority Queue
    def length(self):
        return len(self.queue)
    
    # Should take the minimum element from the Priority Queue and return it       
    def dequeue(self):
        popped_node = self.queue.pop(0)
        return popped_node

    # Removes a specific node in the Priority Queue
    def removal(self, node):
        self.queue.remove(node)

    # Should add an element or elements to the Priority Queue
    def enqueue(self, el):
        self.queue.append(el)

    # Gets the node with the smallest Cost or highest Priority
    def get_smallest(self, pri_queue):

        smallest_num = float("inf")
        smallest_node = None

        for node in pri_queue:
            number = node.value

            if number < smallest_num:
                smallest_num = number
                smallest_node = node

        return smallest_node

    # Gets the node with the smallest heuristic or highest Priority
    # def get_smallest_heuristic(self, pri_queue):

    #     smallest_num = float("inf")
    #     smallest_node = None

    #     for node in pri_queue:
    #         number = node.heurist

    #         if number < smallest_num:
    #             smallest_num = number
    #             smallest_node = node

    #     return smallest_node

    # Sorts the Queue according to the priority of the nodes
    def reorder(self):

        smallest_num = float("inf")
        smallest_node = None
        new_queue = list()

        while len(self.queue) != 0:
            
            smallest_node = self.get_smallest(self.queue)

            new_queue.append(smallest_node)
            self.queue.remove(smallest_node)

        self.queue = new_queue

# ** ONLY DO THIS IF YOU WANT BONUS MARKS**
# MinHeap allows you to extract elements in O(logn) time
# Feel free to add more helper functions
class MinHeap:
    
    
    def __init__(self):
        self.heap = []
    
    
    # ** FINISH THIS FUNCTION **
    # Adds element to heap

    def enqueue(self, el):
        pass
    
    
    
    # ** FINISH THIS FUNCTION **
    # Should take minmum element from heap and return element

    def dequeue(self):
        pass
    

# ---------------------- My Node Class ------------------#
class Node:

    def __init__(self, label, cost, path, total, heurist=0):
        self.label = label
        self.cost = cost
        self.path = path + self.label
        self.total = total + self.cost

        self.value = self.total + heurist # The value or Priority

    # Returns a string of the Node - for testing
    def __str__(self):
        return str((self.label, self.cost))

    # Returns the 'Current Path' and 'Overall Cost' to this node
    def __repr__(self):
        return ( list(self.path), self.total )
#--------------------------------------------------------#

# Returns the children/negihbours of a node in the graph including path cost
# e.g. [('A', 20), ('B', 30), ('D', 50)]
# graph - dictionary of nodes and edges
# node - label of node
def get_children(graph, node):
    children = []
    if node in graph.keys():
        children = list(graph[node].items())
    return children


# ** FINISH THIS FUNCTION **
# Should return a list representing the path from start to goal
# e.g ['A', 'B', 'G'] would be a possible solution starting from start node A to goal node G
# If there is no path from start to goal, the function should return empty list
# path_graph - dictionary of nodes and edges
# heurist_dist - dictionary of heuristic distance to goal
# start - label for start node e.g. 'A'
# goal - label for goal node e.g. 'G'
# search_type - can be one of UCS, Greedy, A-Start
# fringe_type - data structure used for fring can be one of p_queue, heap
def path_find(path_graph, heurist_dist, start, goal, 
				search_type='UCS', fringe_type='p_queue'):
    
    if fringe_type == 'p_queue':
        fringe = PriorityQueue()
    else:
        fringe = MinHeap()
    
    # start_node = Node(start, None)
    # goal_node = Node(goal, None)
    
    # visited = []
    # goal_found = False
    # fringe.enqueue(start_node) # add the start node to fringe

    # Does what it needs to do based on 'search_type'
    if search_type == "UCS":
        result = my_ucs(start, path_graph, fringe, goal)
        return list(result)

    elif search_type == "Greedy":
        result = my_greedy(start, path_graph, heurist_dist, fringe, goal)
        return list(result)

    elif search_type == "A-Star":
        result = my_star(start, path_graph, heurist_dist, fringe, goal)
        return list(result)

    return [] # Return an empty list if anything else
    

def my_ucs(start, graph, fringe, goal):
    
    start_node = Node(start, 0, "", 0)
    fringe.enqueue(start_node) # Adds the start node to fringe

    # Loops until the Priority Queue is empty
    while fringe.length() != 0:
        next_node = fringe.dequeue()

        # Check for Goal Node
        if next_node.label == goal:
            return next_node.path

        # This check is insurance for empty nodes not declared in the graph
        if next_node.label not in graph.keys():
            node_children = []
        else:
            node_children = get_children(graph, next_node.label)

        # Now we need to add these children to the Priority Queue
        for child in node_children:
            label = child[0]
            cost = child[1]

            new_node = Node(label, cost, next_node.path, next_node.total) # Creates the new node
            fringe.enqueue(new_node) # Adds the new node to fringe

        # Reoorder the Priority Queue
        fringe.reorder()

def my_greedy(start, graph, heuristic_graph, fringe, goal):

    start_node = Node(start, 0, "", 0)
    fringe.enqueue(start_node) # Adds the start node to fringe

    # Loops until the Stack is empty
    while fringe.length() != 0:
        next_node = fringe.dequeue() # Or pop, same thing

        # Check for Goal Node
        if next_node.label == goal:
            return next_node.path

        # This check is insurance for empty nodes not declared in the graph
        if next_node.label not in graph.keys():
            node_children = []
        else:
            node_children = get_children(graph, next_node.label)

        # Now we need to add these children to the Priority Queue
        for child in node_children:
            label = child[0]
            cost = heuristic_graph[label]

            new_node = Node(label, cost, next_node.path, next_node.total) # Creates the new node
            fringe.enqueue(new_node) # Adds the new node to fringe

        # Reoorder the Priority Queue
        fringe.reorder()

def my_star(start, graph, heuristic_graph, fringe, goal):

    # Removes all the nodes that have been visited
    def remove_visited(keys, pri_queue):
        new_queue = list()

        if len(keys) == 0:
            return pri_queue

        for node in pri_queue:
            if node.label not in keys:
                new_queue.append(node)

        return new_queue
    #----------------------------------------------
    
    start_node = Node(start, 0, "", 0)
    fringe.enqueue(start_node) # Adds the start node to fringe
    visited = []

    while True:
        next_node = fringe.dequeue()

        # Update the Visited node
        visited.append(next_node.label)

        # Check for Goal Node
        if next_node.label == goal:
            return next_node.path

        # This check is insurance for empty nodes not declared in the graph
        if next_node.label not in graph.keys():
            node_children = []
        else:
            node_children = get_children(graph, next_node.label)

        # Now we need to add these children
        # temp_list = list()
        for child in node_children:
            key = child[0]
            cost = child[1]
            heuristic_value = heuristic_graph[key]

            if key in visited:
                continue
            # new_value = (cost + next_node.total) + heurist

            new_node = Node(key, cost, next_node.path, next_node.total, heuristic_value)
            # new_node.heurist = new_node.total + heuristic_value
            # temp_list.append(new_node)
            fringe.enqueue(new_node)

        # Reoorder the Priority Queue
        fringe.reorder()


# Main
if __name__ == "__main__":
    graph = {
	    'A': {'B': 20, 'D': 80, 'G': 95},
	    'B' : {'E': 50, 'F': 10},
	    'C' : {'D': 50, 'H': 20},
	    'D' : {'G': 10},
	    'F' : {'D': 40, 'C': 10}
    }

    graph2 = {    
        'A': {'Z': 75, 'T': 118, 'S': 140},
        'B' : {'G': 90, 'U': 85, 'P': 101, 'F': 211},
        'C' : {'P': 138, 'R': 146, 'D': 120},
        'D' : {'M': 75, 'C': 120},
        'E' : {'H': 86},
        'F' : {'S': 99, 'B': 211},
        'G' : {'B': 90},
        'H' : {'U': 98, 'E': 86},
        'I' : {'N': 87, 'V': 92},
        'L' : {'T': 111, 'M': 70},
        'M' : {'L': 70, 'D': 75},
        'N' : {'I': 87},
        'O' : {'Z': 71, 'S': 151},
        'P' : {'R': 97, 'B': 101, 'C': 138},
        'R' : {'S': 80, 'P': 97, 'C': 146},
        'S' : {'A': 140, 'O': 151, 'R': 80},
        'T' : {'A': 118, 'L': 70},
        'U' : {'B': 85, 'H': 98, 'V': 142},
        'V' : {'I': 92, 'U': 142},
        'Z' : {'A': 75, 'O': 71}
    }

    heurist_dist = {
        'A': 90,
        'B': 55,
        'C': 55,
        'D': 8,
        'E': 100,
        'F': 45,
        'G': 0,
        'H': 100
    }

    heurist_dist2 = {
        'A': 366,
        'B': 0,
        'C': 160,
        'D': 242,
        'E': 161,
        'F': 176,
        'G': 77,
        'H': 151,
        'I': 226,
        'L': 224,
        'M': 241,
        'N': 234,
        'O': 380,
        'P': 100,
        'R': 193,
        'S': 253,
        'T': 329,
        'U': 80,
        'V': 199,
        'Z': 374
    }

    # # Testing Functions
    # result = get_children(graph, "A")

    fringe = PriorityQueue()
    # result = path_find(graph, heurist_dist, 'A', 'G', search_type='A-Star', fringe_type='p_queue') #['A', 'B', 'F', 'D', 'G']
    # result = path_find(graph2, heurist_dist2, 'A', 'B', search_type='A-Star', fringe_type='p_queue') #['A', 'S', 'R', 'P', 'B']
    # result = path_find(graph2, heurist_dist2, 'T', 'B', search_type='A-Star', fringe_type='p_queue') #['T', 'A', 'S', 'R', 'P', 'B']
    # result = path_find(graph, heurist_dist, 'F', 'G', search_type='UCS', fringe_type='p_queue') #['F', 'D', 'G']
    # result = path_find(graph2, heurist_dist2, 'A', 'B', search_type='Greedy', fringe_type='p_queue') #['A', 'S', 'R', 'P', 'B']
    # result = path_find(graph2, heurist_dist2, 'T', 'B', search_type='UCS', fringe_type='p_queue') #['T', 'A', 'S', 'R', 'P', 'B']
    # result = path_find(graph2, heurist_dist2, 'O', 'B', search_type='Greedy', fringe_type='p_queue') #['O', 'S', 'R', 'P', 'B']
    # result = path_find(graph2, heurist_dist2, 'O', 'B', search_type='UCS', fringe_type='p_queue') #['O', 'S', 'R', 'P', 'B']
    # result = path_find(graph, heurist_dist, 'A', 'G', search_type='Greedy', fringe_type='p_queue') #['A', 'G']
    result = path_find(graph2, heurist_dist2, 'D', 'B', search_type='UCS', fringe_type='p_queue') #['D', 'C', 'P', 'B']

    # result = path_find(graph, heurist_dist, 'A', 'G', search_type='A-Star', fringe_type='p_queue')
    print(result)