from data_structures_and_algorithms401.tree.tree import *

    
def test_find_maximum_value_one():
    bt=BinaryTree()
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(100)
    bt.root.right.right = Node(-4)
    actual=bt.find_maximum_value()
    expected=50
    assert actual == expected

def test_find_maximum_value_for_negative():
    bt=BinaryTree()
    bt = BinaryTree()
    bt.root = Node(-7)
    bt.root.left = Node(-13)
    bt.root.right = Node(-5)
    bt.root.left.left = Node(-8)
    bt.root.left.right = Node(-9)
    bt.root.right.left = Node(-100)
    bt.root.right.right = Node(-4)
    actual=bt.find_maximum_value()
    expected=-4
    assert actual == expected

    
def test_find_maximum_value_if_we_have_left_right_only():
    bt=BinaryTree()
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    actual=bt.find_maximum_value()
    expected=13
    assert actual == expected

def test_find_maximum_value_if_we_have_only_one_node():
    bt=BinaryTree()
    bt = BinaryTree()
    bt.root = Node(7)
    actual=bt.find_maximum_value()
    expected=7
    assert actual == expected
