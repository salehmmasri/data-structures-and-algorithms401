from data_structures_and_algorithms401.mearge_sort.mearge_sort import mergeSort

def test_merge_sort_negative_val():
    arr=[20,18,12,8,5,-2]
    expected=[-2, 5, 8, 12, 18, 20]
    actual=mergeSort(arr)
    assert actual == expected

def test_merge_sort():
    arr=[8,4,23,42,16,15]
    expected=[4, 8, 15, 16, 23, 42]
    actual=mergeSort(arr)
    assert actual == expected
    

def test_merge_sort_equal_vals():
    arr=[5,12,7,5,5,7]
    expected=[5, 5, 5, 7, 7, 12]
    actual=mergeSort(arr)
    assert actual == expected

def test_merge_sort_normal_vals():
    arr=[2,3,5,7,13,11]
    expected=[2, 3, 5, 7, 11, 13]
    actual=mergeSort(arr)
    assert actual == expected
