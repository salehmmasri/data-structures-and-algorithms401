class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value, root=None):
        node = _Node(value)
        root = root or self.root

        if not root:
            self.root = node
            return

        if value < root.value:
            if root.left:
                self.add(value, root.left)
            else:
                root.left = node
        if value > root.value:
            if root.right:
                self.add(value, root.right)
            else:
                root.right = node


def fizz_buzz_tree(tree, root=None, action=None):
    root = root or tree.root
    if not action:
        action = fizz_buzz_func
    if root:
        root.value = action(root.value)
        if root.left:
            fizz_buzz_tree(tree, root.left)
        if root.right:
            fizz_buzz_tree(tree, root.right)      
    else:
        return "Empty Tree"
    return tree


def fizz_buzz_func(value):
    if value%3 == 0 and value%5 == 0:
        return "FizzBuzz"
    if value%3 == 0:
        return "Fizz"
    if value%5 == 0:
        return "Buzz"
    value = str(value)
    return value
if __name__ == "__main__":
    # tree = BinaryTree()
    # tree.add(10)
    # tree.add(15)
    # tree.add(20)
    # tree.add(22)
    # tree.add(91)
    # tree.add(3000)
    # tree = fizz_buzz_tree(tree)
    # print( tree.root.value == 'Buzz')
    # print( tree.root.right.right.right.right.right.value == 'FizzBuzz')
    pass