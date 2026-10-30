
#parent/super/base class
class Animal:
    isMammal = True
    gender = "male"
    age = 2

    def movement(self):
        print("Animal is moving")

class Cow(Animal): #child class/sub class/Derived class
    def moow(self):
        print("Cow is moowing")

class Cat(Animal): #child class
    def meow(self):
        print("Cat is meowing")

mycow = Cow()
mycow.moow()

mycat = Cat()
mycat.meow()