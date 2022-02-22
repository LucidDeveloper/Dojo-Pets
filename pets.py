'''@ author
Gianni M. Javier
'''

# NINJA BONUS: Use modules to separate out the classes into different files.

# Create a Pet class with the pet attributes listed in the assignment.
class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self,name,type,tricks, energy, health):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health

# Implement sleep(), eat(), play(), noise() methods on the pet class.
# implement the following methods:

# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

# noise() - prints out the pet's sound
    def noise(self):
        return self

# SENSEI BONUS: Use Inheritance to create sub classes of pets
class Cat(Pet): # Inheritance used to inherit all attributes and methods of Parent Class
# special method super() used to call upon Pet atrtibutes and append new attributes.
    def __init__(self,name,type,tricks, energy, health):
        super().__init__(name,type,tricks,energy,health)
    # noise() - prints out the pet's sound
    def noise(self):
        print('Meow!')
        return self

class Dog(Pet): # inheritance used to inherit all attributes and methods of Parent class
# special method super() used to call upon Pet attributes and append new attributes.
    def __init__(self,name,type,tricks, energy, health):
        super().__init__(name,type,tricks,energy,health)
    # noise() - prints out the pet's sound
    def noise(self):
        print('Bark!')
        return self