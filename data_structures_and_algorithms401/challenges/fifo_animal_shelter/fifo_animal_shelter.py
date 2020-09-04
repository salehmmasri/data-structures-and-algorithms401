class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, *value):
        for j in value:
            node = Node(j)
            if not self.front and not self.rear:
                self.front = node
                self.rear = node
            old_rear = self.rear
            self.rear = node
            old_rear.next = self.rear

    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            return temp
        else:
            return "Q is empty"
    
    def peek(self):
        try:
            return self.front.value
        except AttributeError as e:
            return f"Empty Queue!!!"
        except Exception as e:
            return f"Some other exception happened!!!"
    def display(self):
            """
            * This function will print all nodes of the Q 
            """
            current = self.front
            output = ''
            while current:
                output += f"|{current.value}|"
                current = current.next
            return output



class AnimalShelter:
    cat = Queue()
    dog = Queue()

    def __init__(self):
        pass

    def __str__(self):
        out2=AnimalShelter.dog.display()
        out2+=AnimalShelter.cat.display()
        return out2
         
    def enqueue(self, value, type_to_add):
        """
        Takes animal and creates new nodes in the queue's based on type_to_add 
        """
        try:
            if type_to_add=='cat':
                AnimalShelter.cat.enqueue(value)
                
            elif type_to_add=='dog':
                AnimalShelter.dog.enqueue(value)        
            else:
                print('you can add only cat or dog')
        except Exception as error:
            return f'Method has an error: {error}'

    def dequeue(self, preferred_animal=None):
        """ 
        Dequeues preferred animal based on the owner type  
        """
        if preferred_animal=='cat':
            AnimalShelter.cat.dequeue()
        elif preferred_animal=='dog':
            AnimalShelter.dog.dequeue()
        else:
            print('you should enter preferred animal to dequeue')

            

if __name__ == "__main__":
    animals = AnimalShelter()
    animals.enqueue('oscar1','dog')
    animals.enqueue('oscar2','dog')
    animals.enqueue('oscar3','dog')
    animals.enqueue('cat1','cat')
    animals.enqueue('cat2','cat')
    animals.enqueue('cat3','cat')
    animals.dequeue('dog')
    animals.dequeue('cat')
    actual=animals
    print(actual)
