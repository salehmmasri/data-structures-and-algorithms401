
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
