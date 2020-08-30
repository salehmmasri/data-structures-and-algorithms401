from data_structures_and_algorithms401.challenges.queue_with_stacks.queue_with_stacks import *

def test_enqueue():
    nums = PseudoQueue()
    nums.enqueue(1)
    nums.enqueue(2)
    nums.enqueue(3)
    nums.enqueue(4)
    actual= nums.__str__()
    expected = "-> { 4 } -> { 3 } -> { 2 } -> { 1 }"
    assert actual == expected

def test_enqueue():
    nums = PseudoQueue()
    nums.enqueue(10)
    nums.enqueue(20)
    nums.enqueue(30)
    nums.enqueue(40)
    actual= nums.__str__()
    expected = "-> { 40 } -> { 30 } -> { 20 } -> { 10 }"
    assert actual == expected

def test_enqueue():
    nums = PseudoQueue()
    nums.enqueue(1)
    nums.enqueue(2)
    nums.enqueue(3)
    nums.enqueue(4)
    actual= nums.dequeue()
    expected = 1
    assert actual == expected

def test_empty_enqueue():
    nums = PseudoQueue()
    actual= nums.dequeue()
    expected ="Empty"
    assert actual == expected