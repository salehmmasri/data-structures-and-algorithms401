class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, *value):
        # Special case: if empty queue
        # f -> 1 <- r
        for j in value:
            node = Node(j)
            if not self.front and not self.rear:
                self.front = node
                self.rear = node
            old_rear = self.rear
            self.rear = node
            old_rear.next = self.rear
            # front -> 1 -> 2 -> 3 <- rear
    def dequeue(self):
        if self.front:
            self.front=self.front.next
        else:
            return "Q is empty"
    def peek(self):
        try:
            return self.front.value
        except AttributeError as e:
            return f"Empty Queue!!!\nDevs Details: {e}"
        except Exception as e:
            return f"Some other exception happened!!! {e}"

    def __str__(self):
        """
        * This function will print all nodes of the Q 
        """
        current = self.front
        output = ''
        while current:
            output += f"|{current.value}|"
            current = current.next
        output=f'Q Front ==> {output}  <== Q Rear'
        return output

    def is_empty(self):
        """
        
        this function cheack if the Q is empty or not 

        """
        if self.front:
            # Q not empty  values
            return False
        else:
            # Q empty
            return True
            
class Stack:
    def __init__(self):
        self.max = 10000
        self.top = None

    def push(self, *value):
        """
        - Create a node with vlaue
        - Add the node to the top of the stack
        - check if top is None:
            - True point top to new node
            - else:
                - save top in temp (temporary)
                - top = the new node
                - reassign top.next to temp
        """
        for i in value:
            node = Node(i)
            temp = self.top # temp = None
            self.top = node # top = node(5)
            self.top.next = temp # node(5).next = None

    def pop(self):
        try:
            self.top = self.top.next # top = node(5)
        except AttributeError as e:
            return f"Empty Queue!!!\nDevs Details: {e}"
        except Exception as e:
            return f"Some other exception happened!!! {e}"
    def peek(self):
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        """
        
        this function cheack if the Stack is empty or not 
        
        """
        if self.top:
            # stack have values 
            return False
        else:
            # stack have no values
            return True
    def __str__(self):
        """
        * This function will print all nodes of the Stack 
        """
        current = self.top
        output = ''
        while current:
            output += f"[{current.value}]"
            current = current.next
        output=f'\n Stack {output}'
        return output


if __name__ == '__main__':
    # # print(eaters.peek())
    eaters = Queue()
    # eaters.enqueue("Saed","Ahmad")
    # eaters.enqueue("Ahmad")
    
    # eaters.enqueue("Ahmad")
    # print(eaters.dequeue()) # should return Saed
    # print(eaters.front.value) # Saed
    # print(eaters.rear.value) # Ahmad
    # print(eaters.peek()) # Saed
    # first_name.push('saleh','moh')
    # eaters.dequeue()
    # eaters.dequeue()

    # print(eaters.peek())
    # eaters.dequeue()
    # eaters.dequeue()
    
    print(eaters.peek())
