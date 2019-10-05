from collections import defaultdict


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def is_cyclic_util(self, v, visited, parent):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False

    # Returns true if the graph contains a cycle, else false.
    def is_cyclic(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if not visited[i]:  # Don't recur for u if it is already visited
                if self.is_cyclic_util(i, visited, -1):
                    return True
        return False


counter = get_number()

while counter > 0:
    number_of_nodes = get_number()
    number_of_vertexes = get_number()
    # If there are more vertexes than nodes there's must be a cycle
    if number_of_vertexes > number_of_nodes:
        while number_of_vertexes > 0:
            get_word(), get_word()
            number_of_vertexes -= 1
        print(1)
    else:
        graph = Graph(number_of_nodes)
        while number_of_vertexes > 0:
            graph.add_edge(get_number(), get_number())
            number_of_vertexes -= 1
        if graph.is_cyclic():
            print(1)
        else:
            print(0)
    counter -= 1
