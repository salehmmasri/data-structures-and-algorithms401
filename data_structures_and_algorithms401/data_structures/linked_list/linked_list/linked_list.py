class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head=None
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

    # def insert_to_the_first(self, value):
    #     new_node=Node(value)
    #     if self.head is None:
    #         self.head=new_node
    #     else:
    #         current=self.head
    #         self.head=new_node
    #         new_node.next=current
    
    def insert_Before(self,value, find_val):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            try:
                current=self.head
                if current.next.value != None:
                    temp=current.next
                while current.next.value != find_val:
                    current=current.next
                if current.next.value == find_val:
                    old=current.next
                    current.next=new_node
                    new_node.next=old
                else :
                    print("hi")
            except:
                print("error")
    def insert_after(self,value, find_val):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            try:
                current=self.head
                while current.value != find_val:
                    current=current.next
                    print("sa")
                if current.value==find_val:
                    print('aaa')
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
    lis= LinkedList()
    lis.append(2)
    lis.append(3)
    actual =lis.__str__()
    print(actual)
    # lls.insert_Before(9,5)
    # fruits = LinkedList()
    # fruits.append(2)
    # fruits.append('saleh')
    # fruits.append('saleh2')
    # fruits.append('saleh3')

    # print(fruits)
    # fruits.insert_Before(5,'6')
    # # fruits.insert_Before(5,'saleh')
    # print('saaaaa')
    # print(fruits)
    # print('after')
    