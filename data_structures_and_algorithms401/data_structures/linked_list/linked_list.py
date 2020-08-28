class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(Node):
    
    def __init__(self):
        self.head=None
        
    def search_for(self,valuenum):
        """
        * This function will search for a value in the Linked list and if it is not in the LL it will return False
        """        
        current = self.head
        while current:
            if current.value == valuenum :
                return True
            else:
                current=current.next
        return False   
    
    def append(self,value):
        """
        * This function will append the new node at the end  of the Linked list 
        """
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def insert_Before(self,value, find_val):
        """
        * This function will insert the new node before the value you enterd and if value you enterd it'is not in the Linked list it will arise a error  
        """
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
        """
        * This function will return the value of the node at specific index in the linked list 
        """
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
        """
        * This function will insert the new node after the value you enterd Linked list 
        """
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
        """
        * This function will print all nodes of the Linked list 
        """
        current = self.head
        output = ''
        while current:
            output += f"{{{current.value}}}-->"
            current = current.next
        output=f'"{output}Null"'
        return output

    def insert(self, value):
        """
        * This function will insert the new node at the begining of the Linked list 
        """
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            self.head=new_node
            new_node.next=current

    # def reverse_ls(llone): 
    #         prev = None
    #         current = llone.head
    #         while(current is not None): 
    #             next = current.next
    #             current.next = prev 
    #             prev = current 
    #             current = next
    #         llone.head = prev 


if __name__=="__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    print(zip_linked_list(ll,ll2))




