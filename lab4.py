#problem 1
class Animal(object):
    def __init__(self,sound,name,age,favorite_color):
            self.sound = sound
            self.name = name
            self.age = age
            self.favorite_color = favorite_color
    def eat(self,food):
        print("Yummy!! " + self.name + " is eating " + food)
    def description(self):
        print(self.name + "is" + self.age +"years old and loves the color "+self.favorite_color)


myanimal = Animal("meaw","rexi",10, "red") #created new object

print(myanimal.name) #printed the object's name

myanimal.eat("tuna")
