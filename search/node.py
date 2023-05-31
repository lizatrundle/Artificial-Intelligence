
 # cost --> g(n)
    # heuristic --> h(n) 
    # function --> f(n) 



    # greedy BFS --> heuristic 
    # uniform cost --> cost 
    # A* --> f(n)
    # include three variables to have three different algorithms in one file 


    # vertex is ID of the node
    #  parent is ID of the parent node
    #  cost is g(n) used by UCS 
    # heruistic is h(n) used by greedy best first search 
   # function is f(n) used by A*


class Node:
    def __init__(self, vertex, parent=None, cost=0, heuristic=0, function=0):
        # heruristic is the value of the heuristic function used by A* 
        # this is the constructor to the class 
        self._vertex = vertex
        self._parent = parent
        self._cost = cost
        self._heuristic = heuristic
        self._function = function

    @property  # avoid formal getters and setters, just getting attributes from the constructor 
    def vertex(self):
        return self._vertex
    
    @property
    def parent(self):
        return self._parent

    @property
    def cost(self):
        return self._cost

    @property
    def heuristic(self):
        return self._heuristic

    @property
    def function(self):
        return self._function

    def __str__(self):
        return "'" + self._vertex + "'" if self._parent == None else "'" + str(self._vertex) + "','" + str(self._parent) + "',cost=" + str(self._cost) + ",heuristic=" + str(self._heuristic)

