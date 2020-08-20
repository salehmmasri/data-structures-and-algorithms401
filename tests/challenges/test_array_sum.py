from data_structures_and_algorithms401.challenges.array_sum.array_sum import *

def test_sumation():
    actual = sum_arrays([[1,2,3],[4,5,6,7],[8,9,10]])
    expected = [6, 22, 17]
    assert actual == expected

def test_if_array_contains_array():
    actual = sum_arrays([1,2,3])
    expected = "this is not array of arrayes"
    assert actual == expected
