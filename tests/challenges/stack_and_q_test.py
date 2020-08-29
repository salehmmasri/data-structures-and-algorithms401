from data_structures_and_algorithms401.stacks_and_queues.stacks_and_queues import (
    Node,Stack,Queue
)
def test_push_onto_a_stack_and_instantiate_an_empty_stack():
    first_name = Stack()
    first_name.push('saleh')
    actual = first_name
    expected = "\n Stack [saleh] \n "
    assert actual == expected
    
def test_push_multiple_values_stack():
    first_name = Stack()
    first_name.push('saleh','moh','ahmad')
    actual = first_name
    expected = "\n Stack [ahmad][moh][saleh]"
    assert actual == expected

def test_pop_stack():
    first_name = Stack()
    first_name.push('saleh','moh','ahmad')
    first_name.pop()
    actual = first_name
    expected = "\n Stack [moh][saleh]"
    assert actual == expected

def test_make_stack_empty():
    first_name = Stack()
    first_name.push('saleh','moh')
    first_name.pop()
    first_name.pop()
    actual = first_name
    expected = "\n Stack "
    assert actual == expected

def test_peek_stack():
    first_name = Stack()
    first_name.push('saleh','moh')
    actual = first_name.peek()
    expected = "moh"
    assert actual == expected

def test_peek_on_empty_stack():
    first_name = Stack()
    actual = first_name.peek()
    expected = "Stack is empty"
    assert actual == expected

def test_enqueue():
    eaters = Queue()
    eaters.enqueue("Saed")
    eaters.enqueue("Ahmad")
    actual = eaters
    expected = "Q Front ==> |Saed||Ahmad|  <== Q Rear"
    assert actual == expected

def test_enqueue_multiple_value():
    eaters = Queue()
    eaters.enqueue("Saed","Ahmad")
    actual = eaters
    expected = "Q Front ==> |Saed||Ahmad|  <== Q Rear"
    assert actual == expected

def test_dequeue():
    eaters = Queue()
    eaters.enqueue("Saed","Ahmad")
    eaters.dequeue()
    actual = eaters
    expected = "Q Front ==> |Ahmad| <== Q Rear"
    assert actual == expected

def test_peek():
    eaters = Queue()
    eaters.enqueue("Saed","Ahmad")
    actual = eaters.peek()
    expected = "Saed"
    assert actual == expected
def test_peek():
    eaters = Queue()
    actual = eaters.peek()
    expected = ""
    assert actual == expected


def test_empty_queue_after_multiple_dequeue():
    eaters = Queue()
    eaters.enqueue("Saed","Ahmad")
    eaters.dequeue()
    eaters.dequeue()
    actual = eaters
    expected = """Empty Queue!!!
    Devs Details: 'NoneType' object has no attribute 'value'"""
    assert actual == expected






