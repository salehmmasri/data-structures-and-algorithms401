from collections import deque

class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """Adds a Node"""

        new_node = Node(value)
        self._adjacency_list[new_node] = []
        return new_node

    def size(self):
        """returns number of values in adjacency list"""

        return len(self._adjacency_list)

    def add_edge(self, start_node, end_node, weight=0):

        if start_node not in self._adjacency_list:
            raise KeyError('Start Node not in graph')

        if end_node not in self._adjacency_list:
            raise KeyError('End Node not in graph')

        adjacencies = self._adjacency_list[start_node]
        adjacencies.append((end_node, weight))

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, node):
        return self._adjacency_list[node]
   
    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]


    def breadth_first(self, node):
            output = []

            def action(node):
                output.append(node.value)
            self.__traverse(node, action)

            return output

    def __traverse(self, node, action):
        q = Queue()
        q.enqueue(node)
        visited = set([node])
        while not q.empty():
            current = q.dequeue()
            for edge in self.get_neighbors(current):
                v = edge[0]
                if v not in visited:
                    visited.add(v)
                    q.enqueue(v)
            action(current)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, value):
        self.q.appendleft(value)

    def dequeue(self):
        return self.q.pop()

    def empty(self):
        return len(self.q) == 0

if __name__ == "__main__":  
    g = Graph()
    v1 = g.add_node('saleh')
    v2 = g.add_node('almasri')
    g.add_edge(v1, v2, 10)
    expected = ['saleh', 'almasri']
    actual = g.breadth_first(v1)
    if expected == actual:
        print(actual)
