
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    
    def __init__(self):
        self.head=None
    def search_for(self,valuenum):
        current = self.head
        while current:
            if current.value == valuenum :
                return True
            else:
                current=current.next
        return False   














            

        
                
        
    def add_in_the_end(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def insert_to_the_first(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            self.head=new_node
            new_node.next=current

    def __str__(self):
        current = self.head
        output = ''
        
        while current:
            output += f"{{{current.value}}}-->"
            current = current.next
        
        output=f'"{output}Null"'
        return output

if __name__=="__main__":
    # fruits = LinkedList()
    # fruits.insert_to_the_first(1)
    # fruits.add_in_the_end(2)
    # fruits.insert_to_the_first(3)
    # fruits.add_in_the_end(4)
    # print(fruits.)
    # ll = LinkedList() 
    
    # ll.add_in_the_end('saleh')
    # ll.insert_to_the_first('aziz')
    # ll.insert_to_the_first('aziz2')
    # ll.add_in_the_end('saleh2')
    
    # print(ll.search_for('saleh2'))


