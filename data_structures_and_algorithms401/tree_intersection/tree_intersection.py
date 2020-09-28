import sys
sys.path.append('/mnt/c/Users/STD/projects/401/data-structures-and-algorithms401')
from data_structures_and_algorithms401.tree.tree import BinaryTree ,Node

def tree_intersection(bt1,bt2):
    output = []
    def _walk(node1,node2):
        if not node1 or not node2:
            return None
        if node1.value == node2.value:
            output.append(node1.value)
        _walk(node1.left,node2.left)
        _walk(node1.right,node2.right)
    _walk(bt1.root,bt2.root)
    if len(output)<1:
        return None
    else:
        return output
if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt1 = BinaryTree()
    bt1.root = Node(1)
    bt1.root.left = Node(8)
    bt1.root.right = Node(9)
    bt1.root.left.left = Node(6)
    bt1.root.left.right = Node(5)
    print(tree_intersection(bt1,bt))







    