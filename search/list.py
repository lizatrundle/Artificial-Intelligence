from search.node import *

# ADT List (superclass). The interface of this class provides the functions:
#
# empty() returns true if the list is empty and false otherwise
# add(node) adds the node at the rear of the list
# remove() removes the node at the front of the list if the list is not empty
# get(vertex) returns the node with id equal to vertex or None if the node is not in the list
# contains(vertex) returns true if the node with id equal to vertex is in the list and false otherwise
# size() returns the size of the list

class List:
    def __init__(self):
        self._nodes = []

    def empty(self):
        return len(self._nodes) == 0

    def add(self, node): 
        self._nodes.append(node)

    def remove(self):
        if not self.empty():
            return self._nodes.pop(0)

        return None

    def get(self, vertex):
        for node in self._nodes:
            if node.vertex == vertex:
                return node

        return None

    def contains(self, vertex):
        for node in self._nodes:
            if node.vertex == vertex:
                return True

        return False

    def size(self):
        return len(self._nodes)

    def __str__(self):
        s = "{ "

        for node in self._nodes:
            s = s + "[" + str(node) + "],"

        s = s[:-1] + " }"

        return s

# ADT Queue is a subclass of List

class Queue(List):
    pass

# ADT Stack is a subclass of List

class Stack(List):
    def remove(self):
        if not self.empty():
            return self._nodes.pop()

        return None

# ADT PriorityQueue is a subclass of List

class PriorityQueue(List):
    def __swap(self, p, q):
        n = self._nodes[p]
        self._nodes[p] = self._nodes[q]
        self._nodes[q] = n

    def __shiftUp(self, parent, child):
        if self._nodes[child].function < self._nodes[parent].function:
            self.__swap(parent, child)

            if parent != 0:
                self.__shiftUp(int((parent - 1)/2), parent)

    def __shiftDown(self, parent):
        last_child = self.size() - 1

        left_child = 2 * parent + 1
        right_child = 2 * parent + 2


        # to get the parent you do (node-1/2 )
        # to get the child you do (2*node +1 (left) or 2*node+2)

        if left_child <= last_child:
            if right_child <= last_child:
                if self._nodes[left_child].function < self._nodes[right_child].function:
                    if self._nodes[parent].function > self._nodes[left_child].function:
                        self.__swap(parent, left_child)
                        self.__shiftDown(left_child)
                else:
                    if self._nodes[parent].function > self._nodes[right_child].function:
                        self.__swap(parent, right_child)
                        self.__shiftDown(right_child)
            else:
                if self._nodes[parent].function > self._nodes[left_child].function:
                    self.__swap(parent, left_child)

    def add(self, node):
        super().add(node)

        p = self.size() - 1

        self.__shiftUp(int((p - 1)/2), p)

    def remove(self):
        if not self.empty():
            root_node = self._nodes[0]
            last_node = self._nodes.pop()

            if not self.empty():
                self._nodes[0] = last_node
                self.__shiftDown(0)

            return root_node

        return None

            # parent = (index-1)/2
            # left child = parent*2 + 1
            # right child = parent *2 + 2



if __name__ == "__main__":

    queue= Queue()
    queue.add("A")
    queue.add("B")
    queue.add("C")
    queue.add("D")

    print("QUEUE", queue)

    while not queue.empty():
        x = queue.remove()
        print(x)

    stack = Stack()
    stack.add("A")
    stack.add("B")
    stack.add("C")
    stack.add("D")

    priority = PriorityQueue()
    priority.add(4)
    priority.add(3)
    priority.add(1)
    priority.add(2)
    priority.add(9)

    print("Priority queue", priority)


    print("STACK", stack)

    while not stack.empty():
        x = stack.remove()
        print(x)
    