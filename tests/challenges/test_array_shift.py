from data_structures_and_algorithms401.challenges.array_shift.array_shift import insertShiftArray
    
    
def test_one():
    actual = [4,8,15,16,23,42]
    expected = insertShiftArray([4,8,15,23,42], 16)
    assert actual == expected

def test_two():
    actual = [2,4,5,6,8]
    expected = insertShiftArray([2,4,6,8], 5)
    assert actual == expected
