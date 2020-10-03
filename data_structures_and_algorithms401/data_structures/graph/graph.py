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

    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')

        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append((end_vertex, weight))
    
    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

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
    graph = Graph()
    end = graph.add_node('coffee')
    start = graph.add_node('muffin')
    graph.add_edge(start, end)
    expected = (end, 0)
    actual = graph._adjacency_list[start][0]
    print (actual) 
    print(expected)