
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
    def get_length(self):
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
            number = node.priority # Gets the Priority

            if number < smallest_num:
                smallest_num = number
                smallest_node = node

        return smallest_node

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
    
    
    def __init__(self, num=26): # If no estimate is provided, use 26 because there are 26 letters in the alphabet
        self.heap = [Node("", -10000, "", -10000)] * num # Filled this list with 'Placeholder Nodes' because of Heap rules explained below
        self.root = 1 # The top of the Heap is index 1, forget about 0 because...
        """
            Heap RULES:
            The parent node is given by : Heap[(i -1) / 2]
            The left child node is given by : Heap[(2 * i) + 1]
            The right child node is given by : Heap[(2 * i) + 2]
        """
        self.length = 0

    # Gets the length of the Priority Queue
    def get_length(self):
        return self.length
    
    # Adds element to heap
    def enqueue(self, node):
        self.length += 1
        self.heap.insert(self.length, node)
        current = self.length

        while self.heap[current].priority < self.heap[current//2].priority:
            self.swap(current, current//2)
            current = current//2
    
    # Should take minmum element from heap and return element
    def dequeue(self):
        last = self.heap[self.root]

        self.heap[self.root] = self.heap[self.length] # This makes the last value/node entered the new 'Top'

        # Replace node with 'Placeholder Node'. We still need the spot, that's why we don't delete
        self.heap[self.length] = Node("", -11111, "", -11111)

        self.length -= 1
        self.reorder(self.root)
        return last

    def swap(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    # This is actually the 'Heapify' function, but I want to use the same function names throughout my code
    def reorder(self, i=1):
 
        # If the node is a not a leaf node and is greater than any of its child nodes
        if not (i >= (self.length//2) and i <= self.length):
            if (self.heap[i].priority > self.heap[2 * i].priority  or  self.heap[i].priority > self.heap[(2 * i) + 1].priority): 
                if self.heap[2 * i].priority < self.heap[(2 * i) + 1].priority:
                    # Swap the node with the left child and then call the reorder function on it
                    self.swap(i, 2 * i)
                    self.reorder(2 * i)
                else:
                    # Swap the node with right child and then call the reorder function on it
                    self.swap(i, (2 * i) + 1)
                    self.reorder((2 * i) + 1)


# ---------------------- My Node Class ------------------#
class Node:
    """
        Each Search Algorithm checks for different 'values', so I made an extra attribute called...
        ... the 'self.priority' which is what my code will check for each node so that I don't have to re-writing code to...
        ... check for different values based on search type. This makes my Node Class flexible enough to work with...
        ... each search type while using the same 3 functions. If my comments aren't clear enough, contact me.
    """

    def __init__(self, label, cost, path, total, heurist=0): # If no heuristic value was provided, use zero
        self.label = label
        self.cost = cost
        self.path = path + self.label
        self.total = total + self.cost

        self.priority = self.total + heurist # The overall value or Priority for the node

    # Returns a string of the Node - for testing
    def __str__(self):
        return str((self.label, self.cost))

    # Returns the 'Current Path' and 'Overall Cost' to this node
    def __repr__(self):
        return f"({list(self.path)}, {self.total})"
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
        fringe = MinHeap(len(heurist_dist)) 
        # ^ I'm using the length of the graph as a 'possible' number of nodes in the Heap
        # Fingers crossed and I hope it's enough 
    
    result = None

    # Does what it needs to do based on 'search_type'
    if search_type == "UCS":
        result = my_ucs(start, path_graph, fringe, goal)

    elif search_type == "Greedy":
        result = my_greedy(start, path_graph, heurist_dist, fringe, goal)

    elif search_type == "A-Star":
        result = my_star(start, path_graph, heurist_dist, fringe, goal)
        
    # Check results
    if result == None:
        return [] # Return an empty list if anything else
    else:
        return list(result)
    

def my_ucs(start, graph, fringe, goal):
    
    start_node = Node(start, 0, "", 0)
    fringe.enqueue(start_node) # Adds the start node to fringe

    # Loops until the Priority Queue is empty
    while fringe.get_length() != 0:
        next_node = fringe.dequeue()

        if next_node == None: # This means no path to GOAL exists
            return []

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
    while fringe.get_length() != 0:
        next_node = fringe.dequeue() # Or pop, same thing

        if next_node == None: # This means no path to GOAL exists
            return []

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

        if next_node == None: # This means no path to GOAL exists
            return []

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
    """
        Did some testing here and there. 
        Was removed.
    """
    pass