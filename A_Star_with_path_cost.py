import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # cost from start node to current node
        self.h = h  # heuristic cost from current node to goal node
        self.f = g + h  # total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar_search(initial_state, goal_state, heuristic, successors):
    open_list = []
    closed_set = set()
    start_node = Node(initial_state)
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            path, cost = get_path_and_cost(current_node)
            return path, cost
        
        closed_set.add(current_node.state)
        for successor, cost in successors(current_node.state):
            if successor in closed_set:
                continue
            g = current_node.g + cost
            h = heuristic(successor, goal_state)
            f = g + h
            successor_node = Node(successor, current_node, g, h)
            if is_node_in_open_list(successor_node, open_list):
                continue
            heapq.heappush(open_list, successor_node)
    
    return None, None

def get_path_and_cost(node):
    path = []
    current = node
    cost = 0
    while current:
        path.append(current.state)
        cost += current.g
        current = current.parent
    path.reverse()
    return path, cost

def is_node_in_open_list(node, open_list):
    for open_node in open_list:
        if open_node.state == node.state and open_node.f <= node.f:
            return True
    return False

# Example usage:
# Define the initial state, goal state, and the heuristic function
initial_state = 'A'
goal_state = 'H'

def heuristic(state, goal_state):
    # Define a heuristic function that estimates the cost from the current state to the goal state
    # In this example, we use a simple dictionary to store the heuristic values for each state
    heuristic_values = {
        'A': 8,
        'B': 6,
        'C': 4,
        'D': 3,
        'E': 2,
        'F': 3,
        'G': 1,
        'H': 0,
    }
    return heuristic_values[state]

# Define the successors function
def successors(state):
    # Define a successors function that returns the possible successors of the given state and their costs
    # In this example, we use a simple dictionary to store the successors for each state along with their costs
    successors = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 5), ('E', 10)],
        'C': [('F', 3)],
        'D': [('G', 6)],
        'E': [('G', 8)],
        'F': [('H', 3)],
        'G': [('H', 2)],
        'H': [],
    }
    return successors[state]

# Solve the problem using A* search
path, cost = astar_search(initial_state, goal_state, heuristic, successors)

# Print the path and cost
if path:
    print("Path found:", path)
    print("Path cost:", cost)
else:
    print("No path found")