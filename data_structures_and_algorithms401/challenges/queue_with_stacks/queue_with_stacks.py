import sys
sys.path.append("/mnt/c/Users/STD/projects/401/data-structures-and-algorithms401/data_structures_and_algorithms401")
from data_structures_and_algorithms401.stacks_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
        self.count = 0
    def enqueue(self,value):
            self.count +=1
            self.in_stack.push(value)
            
    def dequeue(self):
        if self.out_stack.is_empty:
            while self.count>0:
                self.out_stack.push(self.in_stack.pop())
                self.count-=1
        return self.out_stack.pop()

    def __str__(self):
        output = ''
        cur =self.in_stack.top
        while cur:
            output+= f' -> {{ {cur.value} }}'
            cur = cur.next
        return output
