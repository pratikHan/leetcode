class Animal(object):
    food = ""
    def get_food(self):
        return self.food

class Bird(Animal):
    food = "insects"

class Reptile(Animal):
    food = "fish"

class Fish(Animal):
    food = "Sea Plants"

class AnimalFactory():
    def createAnimal(self,type):
        targetClass = type.capitalize()
        return globals()[targetClass]()

anim = AnimalFactory()
animals = ["animal","bird","reptile","fish"]
for a in animals:
    print(anim.createAnimal(a).get_food())