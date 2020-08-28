from data_structures_and_algorithms401.data_structures.linked_list import linked_list    

            
def zip_linked_list(ll1,ll2):
    """
    * This function will compine two Linked list and return new Linked list 
    """

    if not ll1:
        return ll2
    if not ll2:
        return ll1
    result=LinkedList()
    current1=ll1.head
    current2=ll2.head
    while current1:
        result.append(current1.value)
        if current2:
            result.append(current2.value)
            current2=current2.next
        current1=current1.next
    while current2:
        result.append(current2.value)
        current2=current2.next
    return result

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
