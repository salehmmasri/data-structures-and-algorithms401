import sys 
sys.path.append('/mnt/c/Users/STD/projects/401/data-structures-and-algorithms401')
from data_structures_and_algorithms401.data_structures.graph.graph import Graph

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

# if __name__ == "__main__":
    # g = Graph()
    # v1 = g.add_node('saleh')
    # v2 = g.add_node('almasri')
    # g.add_edge(v1, v2, 10)
    # expected = ['saleh', 'almasri']
    # actual = g.breadth_first(v1)
    # if expected == actual:
    #     print(actual)