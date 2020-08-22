from data_structures_and_algorithms401.challenges.linked_list.linked_list import *
def test_append_to_empty_ll():
    ll = LinkedList()
    ll.add_in_the_end(5)
    assert ll.head.value == 5

def test_append():
    ll = LinkedList()
    ll.add_in_the_end('saleh')
    ll.add_in_the_end('aziz')
    assert ll.head.value == 'saleh'
    assert ll.head.next.value == 'aziz'
    
def test_insert_to_the_first_empty():
    ll = LinkedList()
    ll.insert_to_the_first('saleh')
    assert ll.head.value == 'saleh'
    
def test_insert_to_the_first_empty():
    ll = LinkedList()
    ll.insert_to_the_first('saleh')
    ll.insert_to_the_first('aziz')
    assert ll.head.next.value == 'saleh'
    assert ll.head.value == 'aziz'

def test_dender_str():
    expected="{aziz}-->{saleh}-->Null"
    ll = LinkedList()
    ll.add_in_the_end('saleh')
    ll.insert_to_the_first('aziz')
    assert ll.__str__() == expected
