from data_structures_and_algorithms401.challenges.linked_list.linked_list import *
def test_append():
    ll = LinkedList()
    ll.append(5)
    assert ll.head.value == 5

def test_append():
    ll = LinkedList()
    ll.append('saleh')
    ll.append('aziz')
    assert ll.head.value == 'saleh'
    assert ll.head.next.value == 'aziz'
    
def test_dender_str():
    expected="{aziz}-->{saleh}-->Null"
    ll = LinkedList()
    ll.append('saleh')
    ll.insert('aziz')
    assert ll.__str__() == expected

def test_insert_Before():
    linkedoop = LinkedList()
    linkedoop.append(1)
    linkedoop.append(2)
    linkedoop.append(3)
    linkedoop.append(4)
    linkedoop.append(5)
    linkedoop.append(6)
    linkedoop.append(7)
    linkedoop.insert_Before(22,3)
    actual=linkedoop
    expected = "{1}-->{2}-->{22}-->{3}-->{4}-->{5}-->{6}-->{7}-->Null"
    assert actual == expected


def test_insert_Before_2():
    linkedoop = LinkedList()
    linkedoop.append(1)
    linkedoop.append(2)
    linkedoop.append(3)
    linkedoop.append(4)
    linkedoop.append(5)
    linkedoop.append(6)
    linkedoop.append(7)
    linkedoop.insert_Before(22,1)
    actual=linkedoop
    expected = "{22}-->{1}-->{2}-->{3}-->{4}-->{5}-->{6}-->{7}-->Null"
    assert actual == expected

def test_insert_after():
    lis= LinkedList()
    lis.append(2)
    lis.append(3)
    actual =lis.insert_after(2,3)
    expected =  "{2}-->{3}-->{2}-->Null"
    assert actual == expected
def test_insert_after():
    lis= LinkedList()
    lis.append(2)
    lis.append(3)
    actual =lis.__str__()
    expected =  "{2}-->{3}-->Null"
    assert actual == expected

def test_kth_greater_than_len():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "value not found"
    actual =ll.kth_from_end(5)
    assert expected == actual

def test_kth_from_end_2():
    ll = LinkedList()
    ll.append('s')
    ll.append('a')
    ll.append('l')
    ll.append('e')
    ll.append('h')
    expected = 's'
    actual =ll.kth_from_end(4)
    assert expected == actual

def test_kth_negative():
    linkedoop = LinkedList()
    linkedoop.append(1)
    linkedoop.append(6)
    linkedoop.append(3)
    linkedoop.append(4)
    expected = 'value not found'
    actual =linkedoop.kth_from_end(-2)
    assert expected == actual

def test_kth_from_end_size_is_one():
    ll = LinkedList()
    ll.append(1)
    expected = 1
    actual =linkedoop.kth_from_end(0)
    assert expected == actual


def test_kth_from_end_happy_path():
    linkedoop = LinkedList()
    linkedoop.append(1)
    linkedoop.append(2)
    linkedoop.append(3)
    linkedoop.append(4)
    linkedoop.append(5)
    linkedoop.append(6)
    linkedoop.append(7)
    actual=linkedoop.kth_from_end(2)
    expected = 5
    assert expected == actual
    






