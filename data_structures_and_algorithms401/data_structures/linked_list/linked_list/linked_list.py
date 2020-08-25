class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(Node):
    
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
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def insert(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            self.head=new_node
            new_node.next=current

    def insert_Before(self,value, find_val):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            try:
                current=self.head
                if current.value == find_val:
                    print('s node',self.head.value)
                    new_node.next=self.head
                    self.head=new_node
                else :
                    while current.next.value != find_val:
                        current=current.next
                    if current.next.value == find_val:
                        old=current.next
                        current.next=new_node
                        new_node.next=old
                    
            except:
                print("error")


    def kth_from_end(self, k):
        try:
            num = -1
            current = self.head
            while current:
                current = current.next
                num = num + 1
            if num >= k:
                current = self.head
                for i in range(num - k):
                    current = current.next
            return current.value
        except:
            return "value not found"    
    
    def insert_after(self,value, find_val):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            try:
                current=self.head
                while current.value != find_val:
                    current=current.next
                if current.value==find_val:
                    temp=current.next
                    current.next=new_node
                    new_node.next=temp
                else:
                    print('else')
            except:
                print('The value is not Exist ')
    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"{{{current.value}}}-->"
            current = current.next
        output=f'"{output}Null"'
        return output

if __name__=="__main__":
    linkedoop = LinkedList()
    linkedoop.append(1)
    linkedoop.append(2)
    linkedoop.append(3)
    linkedoop.append(4)
    linkedoop.append(5)
    linkedoop.append(6)
    linkedoop.append(7)
    linkedoop.insert_Before(22,1)
    print(linkedoop)