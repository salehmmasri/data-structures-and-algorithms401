from data_structures_and_algorithms401.challenges.linked_list.linked_list import *
from data_structures_and_algorithms401.ll_zip import *

def test_zip_one():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    expected="{1}-->{5}-->{3}-->{9}-->{2}-->{4}-->Null"
    actual=zip_linked_list(ll,ll2)
    assert actual == expected

def test_zip_emptyll():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(3)
    ll2.append(9)
    expected="{5}-->{3}-->{9}-->Null"
    actual=zip_linked_list(ll,ll2)
    assert actual == expected

def test_zip_emptyll2():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll2 = LinkedList()
    expected="{1}-->{3}-->{2}-->Null"
    actual=zip_linked_list(ll,ll2)
    assert actual == expected
