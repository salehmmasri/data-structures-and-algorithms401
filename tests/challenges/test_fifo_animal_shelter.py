from data_structures_and_algorithms401.challenges.fifo_animal_shelter import *
def test_fifo_animal_shelter_enqueue():
    animals = AnimalShelter()
    animals.enqueue('oscar1','dog')
    animals.enqueue('oscar2','dog')
    animals.enqueue('oscar3','dog')
    animals.enqueue('cat1','cat')
    animals.enqueue('cat2','cat')
    animals.enqueue('cat3','cat')
    actual=animals
    expected='|oscar1||oscar2||oscar3||cat1||cat2||cat3|'
    assert actual == expected

def test_fifo_animal_shelter_dequeue_from_cat():
    animals = AnimalShelter()
    animals.enqueue('oscar1','dog')
    animals.enqueue('oscar2','dog')
    animals.enqueue('oscar3','dog')
    animals.enqueue('cat1','cat')
    animals.enqueue('cat2','cat')
    animals.enqueue('cat3','cat')
    animals.dequeue('cat')
    actual=animals
    expected='|oscar1||oscar2||oscar3||cat2||cat3|'
    assert actual == expected

def test_fifo_animal_shelter_dequeue_from_dog():
    animals = AnimalShelter()
    animals.enqueue('oscar1','dog')
    animals.enqueue('oscar2','dog')
    animals.enqueue('oscar3','dog')
    animals.enqueue('cat1','cat')
    animals.enqueue('cat2','cat')
    animals.enqueue('cat3','cat')
    animals.dequeue('dog')
    actual=animals
    expected='|oscar2||oscar3||cat1||cat2||cat3|'
    assert actual == expected

def test_fifo_animal_shelter_dequeue_from_dog_and_dog():
    animals = AnimalShelter()
    animals.enqueue('oscar1','dog')
    animals.enqueue('oscar2','dog')
    animals.enqueue('oscar3','dog')
    animals.enqueue('cat1','cat')
    animals.enqueue('cat2','cat')
    animals.enqueue('cat3','cat')
    animals.dequeue('dog')
    animals.dequeue('dog')
    actual=animals
    expected='|oscar2||oscar3||cat2||cat3|'
    assert actual == expected