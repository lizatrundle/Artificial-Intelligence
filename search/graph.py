from search.list import *
from search.searchPath import * 
from search.node import *

INFINITE = 2**16

def uniform_cost_search(g,h):
    return g 

def greedy_search(g,h):
    return h 

def astar_search(g,h):
    return g+ h

# Weighted Graph based on a dictionary (key, value), each vertex (key) has a list of edges (value),
# where each edge is represented with a list containing the vertex and the cost
# the heuristic function is used by Greedy Best-first search and A* search (but not by dfs or bfs)


# graph represented as an adjacency list --> a list of lists 


# graph = { vertex-1: [[vertex-1-1, cost-1-1], [vertex-1-2, cost-1-2] ... [vertex-1-m, cost-1-m]],
#           vertex-2: [[vertex-2-1, cost-2-1], [vertex-2-2, cost-2-2] ... [vertex-2-m, cost-2-m]],
#           ...
#           vertex-n: [[vertex-n-1, cost-n-1], [vertex-n-2, cost-n-2] ... [vertex-n-m, cost-n-m]] }
#
# heuristic  = { vertex-1: [heuristic-1],
#                vertex-2: [heuristic-2],
#                ...
#                vertex-n: [heuristic-n] }

class Graph:
    def __init__(self, graph=None, heuristic=None):
        self._graph = {} if graph is None else graph
        self._heuristic = {} if heuristic is None else heuristic


    def get_cost(self, source, destination):
        # get cost from the source to the destination--> this is g() function, this is not the heuristic 
        if source in self._graph:
            for vertex in self._graph[source]:
                if (vertex[0] == destination):
                    return vertex[1] # return the cost of the edge, the second item in the edge list 

        # if not found, return infinity, since the cost is infinity if there is no edge in the graph to destination
        return INFINITE    

    def set_vertex(self, vertex, edges=None, heuristic=None):
        if vertex not in self._graph:
            self._graph[vertex] = [] if edges is None else edges
            self._heuristic[vertex] = [0] if heuristic is None else heuristic



    # method to print the graph when we call print 

    def __str__(self):
        graph = "\n{"

        for vertex in self._graph:
            graph = graph + "\n'" + vertex + "': " + str(self._graph[vertex]) + ", "

        graph = graph[:-2] + "\n}"
        vertices = "{"
        for vertex in self._heuristic:
            vertices = vertices + "'" + vertex + "':" + str(self._heuristic[vertex]) + ", "

        vertices = vertices[:-2] + "}\n"
        return graph + "\n" + vertices if len(vertices) > 1 else graph


    def __retrieve_search_path(self, initial, node, explored):
            path = Stack()
            cost = 0
            while node.parent is not None:
                path.add(node)

                cost = cost + self.get_cost(node.parent, node.vertex)

                node = explored.get(node.parent)
            path.add(Node(initial))
            return SearchPath(path, cost, explored.size())

    # search algorithms: Breadth-first search (BFS), Depth-first search (DFS), A* search



    def bfs(self, initial, goal):


        explored = List()
        # Breadth-first search (BFS) uses a queue as frontier
        frontier = Queue()
        # everytime you add to the queue, make a new node using the Node class 
        frontier.add(Node(initial))

        while not frontier.empty():
            node = frontier.remove()

            if not explored.contains(node.vertex):
                explored.add(node)

                # if the goal state is found, return the solution to the search problem

                if node.vertex == goal:
                    return self.__retrieve_search_path(initial, node, explored)
                # add successors to the frontier
                successors = self._graph[node.vertex]

                for successor in successors: # loop throguh the list of sucessors 
                    successor_node = successor[0]   # the node
                    successor_cost = successor[1]   # the cost 

                    # if the successor has not been explored, add it to the frontier
                    if not explored.contains(successor_node):
                        frontier.add(Node(successor_node, node.vertex, successor_cost))
                        # node.vertex symbolizes the parent node, this allows us to get the path 

        return SearchPath(Stack(), INFINITE)  
         # empty and has infinite nodes --> return this because we didnt find the goal state 



    def dfs(self, initial, goal):


            explored = List()

            # Breadth-first search (BFS) uses a queue as frontier

            frontier = Stack()

            # everytime you add to the queue, make a new node using the Node class 
            frontier.add(Node(initial))
            while not frontier.empty():
                node = frontier.remove()

                if not explored.contains(node.vertex):
                    explored.add(node)

                    # if the goal state is found, return the solution to the search problem

                    if node.vertex == goal:
                        return self.__retrieve_search_path(initial, node, explored)
                    # add successors to the frontier
                    successors = reversed(self._graph[node.vertex])

                    for successor in successors: # loop throguh the list of sucessors 
                        successor_node = successor[0]   # the node
                        successor_cost = successor[1]   # the cost 

                        # if the successor has not been explored, add it to the frontier

                        if not explored.contains(successor_node):
                            frontier.add(Node(successor_node, node.vertex, successor_cost))
                            # node.vertex symbolizes the parent node, this allows us to get the path 

            return SearchPath(Stack(), INFINITE)  
            # empty and has infinite nodes --> return this because we didnt find the goal state 



# since UCS, GBFS, A* all use PQ and the same idea of the algorithm, we can combine them into one method and then apply a different function depending 
# on which we are using 
    def astar(self, initial, goal, function=astar_search):
        explored = List()
        frontier = PriorityQueue()
        frontier.add(Node(initial))

        while not frontier.empty():
                node = frontier.remove()

                if not explored.contains(node.vertex):
                    explored.add(node)
                    # if the goal state is found, return the solution to the search problem
                    if node.vertex == goal:
                        return self.__retrieve_search_path(initial, node, explored)

                    # add successors to the frontier
                    successors = self._graph[node.vertex]

                    for successor in successors: # loop throguh the list of sucessors 
                        successor_node = successor[0]   # the node
                        successor_cost = successor[1]   # the cost 
                        # if the successor has not been explored, add it to the frontier

                        if not explored.contains(successor_node):
                            # g(n) is the cost to get to node n from intiial
                            gn = int(node.cost + successor_cost)

                            # h(n) is the estimated cost to reach goal state from n 
                            hn = int(self._heuristic[successor_node][0])

                            # f(n) is the heuristic function --> the combine of g and h 

                            fn = function(gn,hn) 

                            frontier.add(Node(successor_node, node.vertex, gn,hn,fn))
                            # node.vertex symbolizes the parent node, this allows us to get the path 

        return SearchPath(Stack(), INFINITE)  



    # BFS (initial, goal)

    # explored = empty list 
    # frontier = empty queue 
    # add initial to frontier 
    # while frontier is not empty 
        # node = remove a node from the frontier 
        # if node.vertex is not in explored 
            # add node to explored 
            # if node == goal 
            #   retrieve the search path 
            # if we dont find goal 
            #  get sucessors of each node
            #  for each sucessor, if sucessor is not in explored, add sucessor to the frontier 


