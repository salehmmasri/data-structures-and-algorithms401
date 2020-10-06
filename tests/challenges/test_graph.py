import sys 
sys.path.append('/mnt/c/Users/STD/projects/401/data-structures-and-algorithms401')
from data_structures_and_algorithms401.data_structures.graph.graph import Graph

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


def test_size():
    graph = Graph()
    graph.add_node('testing')
    expected = 1
    actual = graph.size()
    assert actual == expected


def test_add_edge_works():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    graph.add_edge(start, end)

def test_add_edge_effect():
    graph = Graph()
    end = graph.add_node('coffee')
    start = graph.add_node('muffin')
    graph.add_edge(start, end)
    expected = (end, 0)
    actual = graph._adjacency_list[start][0]
    assert actual == expected

def test_add_edge_effect_with_weight():
    graph = Graph()
    end = graph.add_node('coffee')
    start = graph.add_node('muffin')
    graph.add_edge(start, end, 44)
    expected = (end, 44)
    actual = graph._adjacency_list[start][0]
    assert actual == expected

def test_get_edges_one_vertex():
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

    actual = g.get_edge(['Mordor'])
    expected = (True, '$0')
    assert actual == expected


def test_get_edges_two_vertex():
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
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Monstropolis', 'Metroville'])
    expected = (True, '$75')
    assert actual == expected

def test_three_vertex():
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
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Pandora', 'Mordor', 'Monstropolis'])
    expected = (True, '$160')
    assert actual == expected


def test_false_get_edges():
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
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Naboo, Pandora'])
    expected = (False, '$0')
    assert actual == expected
