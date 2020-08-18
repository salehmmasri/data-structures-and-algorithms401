from data_structures_and_algorithms401.challenges.array_binary_search.array_binary_search import *

def test_forval_in_mid():
    actual = binary_search([ 2, 3, 4, 10, 40 ], 0, 4, 10)
    expected = 3
    assert actual == expected

def test_forval_max():
    actual = binary_search([ 10, 20, 30, 40, 50 , 60, 70, 80 ], 0, 7, 80)
    expected = 7
    assert actual == expected
def test_forval_nothear():
    actual = binary_search([ 10, 20, 30, 40, 50 , 60, 70, 80 ], 0, 7, 100)
    expected = -1
    assert actual == expected
