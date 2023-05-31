# SearchPath objects are used to return the solution of a search problem 



# the @property is used for private classes, so that we can access the private attributes 
class SearchPath:
    def __init__(self, path, cost, explored_nodes= None):
        self._path = path
        self._cost = cost
        self._explored_nodes = explored_nodes

    @property
    def path(self):
        return self._path

    @property
    def cost(self):
        return self._cost

    @property
    def explored_nodes(self):
        return self._explored_nodes
