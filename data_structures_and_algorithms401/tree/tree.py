class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        try:    
            """
            function return array depending on pre order traversal 
            """
            output = []
            def _walk(node):
                if not node:
                    return
                output.append(node.value)
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)
            return output
        except:
            print("something wrong happened try again")

    def inOrder(self):
        try:    
            """
            function return array depending on in order traversal 
            """
            output = []
            def _walk(node):
                if not node:
                    return
                _walk(node.left)
                output.append(node.value)
                _walk(node.right)
            _walk(self.root)
            return output
        except:
            print("something wrong happened try again")

    def postOrder(self):
        """
        function return array depending on post order traversal 
        """
        try:
            output = []
            def _walk(node):
                if not node:
                    return
                _walk(node.left)
                _walk(node.right)
                output.append(node.value)
            _walk(self.root)
            return output
        except:
            print("something wrong happened try again")       



    def __str__(self):
        """
        function to print the tree 
        """
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)
        
        _walk(self.root)
        return f'tree {output}'


class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        """
        function to add new values to the tree 
        """
        try:
            if not self.root:
                self.root = Node(value)
            else:
                current = self.root
                while (current):
                    if current.value > value: # Got to left
                        if current.left == None: # if current is a leaf
                            current.left = Node(value)
                            break
                        current = current.left
                    else:
                        if current.right == None: # if current is a leaf
                            current.right = Node(value)
                            break
                        current = current.right
        except:
            print("something wrong happened try again")       
    
    
    def contains(self, value):
        """
        function return true if the tree contain the value or value not found 
        """
        try:
            if not self.root:
                return 'value not found'
            else:
                current = self.root
                while (current):
                    if current.value==value:
                        return True
                    if current.value > value: 
                        if current.left == None: 
                            return 'value not found'
                        current = current.left
                    else:
                        if current.right == None: 
                            return 'value not found'
                        current = current.right
        except:
            print("something wrong happened try again")       
                

if __name__=='__main__':
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(10)
    bst.add(12)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    bst.add(50)
    print(bst.postOrder())
