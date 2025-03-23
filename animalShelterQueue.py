# Design an Animal shelter that holds only dogs and cats - FIFO operation  - Adopt the oldest or select a oldest dog or oldest cat

class AnimalQueue:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.age = 0
    
    def enqueue(self,AnimalType):
        self.age += 1
        if AnimalType == 0:
            self.cats.append(self.age)
        else:
            self.dogs.append(self.age)
    
    def dequeueAny(self):
        if self.cats and self.dogs:
            if self.cats[0] > self.dogs[0]:
                return self.dogs.pop(0)
            else:
                return self.cats.pop(0)
        elif self.cats:
            return self.cats.pop(0)
        elif self.dogs:
            return self.dogs.pop(0)
        else:
            print("Queue is empty")
            return -1
        
    def dequeueCat(self):
        if self.cats:
            return self.cats.pop(0)
        else:
            print("Cat list is empty")
            return -1
    
    def dequeueDog(self):
        if self.dogs:
            return self.dogs.pop(0)
        else:
            print("Dog queue is empty")
            return -1
    
    def display(self):
        print("Current cats")
        if self.cats:
            for i in range(len(self.cats)):
                print(self.cats[i], end = '->')
        print("Current dogs")
        if self.dogs:
            for i in range(len(self.dogs)):
                print(self.dogs[i], end = '->')


Animals = AnimalQueue()
size = int(input("Enter number of animals"))
for i in range(size):
    Animals.enqueue(int(input("Enter the animal type")))

Animals.dequeueAny()
Animals.display()
Animals.dequeueCat()
Animals.dequeueCat()
Animals.display()
Animals.dequeueDog()
Animals.enqueue(1)
Animals.display()



    