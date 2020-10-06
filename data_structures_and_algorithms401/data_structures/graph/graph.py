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

    def add_nondirectional_edge(self, start_node, end_node, weight=0):
            self.add_edge(start_node,  end_node, weight)
            self.add_edge( end_node, start_node, weight)
    
    def get_edge(self, v_lst):

        def contains_vertex(value, lst):
            for vertex in lst:
                if isinstance(vertex, tuple):
                    if vertex[0].value == value:
                        return vertex
                    continue
                if vertex.value == value:
                    return vertex
            return False, 0

        current = contains_vertex(v_lst[0], self._adjacency_list.keys())
        if isinstance(current, Node):
            tsum = 0
            for index in range(1, len(v_lst)):
                current, cost = contains_vertex(v_lst[index], self.get_neighbors(current))
                tsum += cost
                if not current:
                    return (False, '$0')
            return (True, f'${tsum}')
        return (False, '$0')



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
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')

    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Mordor','Monstropolis'])
    expected = (True, '$0')
    print('actual',actual)
    print('expected',expected)
