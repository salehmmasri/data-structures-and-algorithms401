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
    def find_maximum_value(self):
        """
            function return the max value in the tree  
        """
        output=self.preOrder()   # => O(n)

        try:
            _max = output[0]
            for i in range(1,len(output)):   # => O(n)
                if _max < output[i]:
                    _max = output[i]
            return _max
        except IndexError as e:
            return f"Your tree might be empty. You got this error: {e}" 
        except Exception as e:
            return f"{e}"

        # twice: 2 * thing   O(2*n)
        # len(thing) * len(thing) O(n^2)



        # pre-order: [1,2,3,4]
        # val = -1M
        # val = 1     i=0
        # val = 2     i=1
        # ...
        # val = 4     i=3             


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
    ^\s*\d{3}-\d{3}-\d{4}\s*$
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(10)
    bst.add(12)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    bst.add(50)
    bt = BinaryTree()
    # print(bt.find_maximum_value())
