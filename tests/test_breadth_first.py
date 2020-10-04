import sys 
sys.path.append('/mnt/c/Users/STD/projects/401/data-structures-and-algorithms401')
from data_structures_and_algorithms401.data_structures.breadth_first.breadth_first import breadth_first

def test_add_node():
    graph = Graph()
    actual = graph.add_node('testing').value
    expected = 'testing'
    assert actual == expected

def test_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected

def breadth_first():
    g = Graph()
    v1 = g.add_node('saleh')
    v2 = g.add_node('almasri')
    g.add_edge(v1, v2, 10)
    expected = ['saleh', 'almasri']
    actual = g.breadth_first(v1)
    assert actual == expected
