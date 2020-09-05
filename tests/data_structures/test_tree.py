from data_structures_and_algorithms401.tree.tree import *

def test_empty_binary_tree():
    bt = BinaryTree()
    assert bt.root == None

def test_single_root_node():
    bt = BinarySearchTree()
    bt.add(20)
    assert bt.root.value== 20

def test_left_child_and_right():
    bt = BinarySearchTree()
    bt.add(20)
    bt.add(10)
    bt.add(30)
    assert bt.root.value == 20
    assert bt.root.left.value == 10
    assert bt.root.left.value == 30

def test_left_postOrder():
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(10)
    bst.add(12)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    bst.add(50)
    actual=bst.preOrder()
    expected='[4, 12, 10, 27, 50, 42, 23]'
    assert actual == expected

def test_preOrder():
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(10)
    bst.add(12)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    bst.add(50)
    actual=bst.preOrder()
    expected='[23, 10, 4, 12, 42, 27, 50]'
    assert actual == expected

def test_inOrder():
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(10)
    bst.add(12)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    bst.add(50)
    actual=bst.inOrder()
    expected='[4, 10, 12, 23, 27, 42, 50]'
    assert actual == expected