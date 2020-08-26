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


    @staticmethod  
    def zipLists(list1,list2):
        nodes_counter_li1 = 0
        nodes_counter_li2 = 0

        current = list1.head
        while current != None:
            current = current.next
            nodes_counter_li1 += 1

        current = list2.head
        while current != None:
            current = current.next
            nodes_counter_li2 = nodes_counter_li2 + 1 

        if nodes_counter_li1 > nodes_counter_li2:
            l1 = list1
            l2 = list2
        else:
            l1 = list2
            l2 = list1

        current = l1.head 
        l2_current = l2.head 
        while current != None and l2_current != None: 
            l1_next = current.next
            l2_next = l2_current.next
            l2_current.next = l1_next 
            current.next = l2_current 
            current = l1_next 
            l2_current = l2_next 
        l2.head = l2_current 
        return l1.toString()

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"{{{current.value}}}-->"
            current = current.next
        output=f'"{output}Null"'
        return output




if __name__=="__main__":
    list_one = LinkedList()
    list_two = LinkedList()
    list_one.append('s')
    list_one.append('a')
    list_one.append('l')
    list_two.append('e')
    list_two.append('h')
    list_two.append('m')
    lis=LinkedList()
    
    # print()



