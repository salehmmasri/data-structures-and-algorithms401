from data_structures_and_algorithms401.challenges.linked_list.linked_list import *
def test_append():
    ll = LinkedList()
    ll.add_in_the_end(5)
    assert ll.head.value == 5

def test_append():
    ll = LinkedList()
    ll.add_in_the_end('saleh')
    ll.add_in_the_end('aziz')
    assert ll.head.value == 'saleh'
    assert ll.head.next.value == 'aziz'
    
def test_dender_str():
    expected="{aziz}-->{saleh}-->Null"
    ll = LinkedList()
    ll.add_in_the_end('saleh')
    ll.insert_to_the_first('aziz')
    assert ll.__str__() == expected

def test_insert_Before():
    lis= LinkedList()
    lis.append(2)
    lis.append(3)
    actual =lis.insert_Before(2,3)
    expected =  "{2}-->{2}-->{3}-->Null"
    assert actual == expected

def test_insert_after():
    lis= LinkedList()
    lis.append(2)
    lis.append(3)
    actual =lis.insert_after(2,3)
    expected =  "{2}-->{3}-->{2}-->Null""
    assert actual == expected
def test_insert_after():
    lis= LinkedList()
    lis.append(2)
    lis.append(3)
    actual =lis.__str__()
    expected =  "{2}-->{3}-->Null""
    assert actual == expected
