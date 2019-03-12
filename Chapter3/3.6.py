#3.6
#Animal Shelter An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
#People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
#or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
#They cannot select which specific animal they would like.
#Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, #and dequeueCat.
#You may use the built-in LinkedList data structure.
#Hints: #22, #56, #63
from Queue import Queue
class AnimalShelter():

    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal.__class__ == Cat:
            self.cats.add(animal.name)
        else:
            self.dogs.add(animal.name)

    def dequeueAny(self):
        if not self.dogs.isEmpty():
            return self.dequeueDog()
        else:
            self.dequeueCat()

    def dequeueCat(self):

        if self.cats.isEmpty():
            return None
        else:
            cat = self.cats.peek()
            self.cats.remove()
            return cat

    def dequeueDog(self):
        if self.dogs.isEmpty():
            return None
        else:
            dog = self.dogs.peek()
            self.dogs.remove()
            return dog

    def print_shelter(self):
        print()
        print('Our Cats : ')
        for i in self.cats.my_queue:
            print(i)
        print()
        print('Our Dogs : ')
        for i in self.dogs.my_queue:
            print(i)
        print()

class Animal():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Cat(Animal): pass
class Dog(Animal): pass

def main():
    myshelter = AnimalShelter()
    mycat = Cat('elena')
    secondcat = Cat('selena')
    puppy = Dog('wolfy')
    dog2 = Dog('tasha')
    mydog = Dog('pups')
    myshelter.enqueue(mycat)
    myshelter.enqueue(secondcat)
    myshelter.enqueue(puppy)
    myshelter.enqueue(dog2)
    myshelter.enqueue(mydog)

    myshelter.print_shelter()

    myshelter.dequeueAny()
    myshelter.dequeueDog()
    myshelter.dequeueCat()

    myshelter.print_shelter()


if __name__ == '__main__':
    main()
