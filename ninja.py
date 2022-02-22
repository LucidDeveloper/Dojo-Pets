''' @ author
Gianni M. Javier
'''

# NINJA BONUS: Use modules to separate out the classes into different files.


# Create a Ninja class with the ninja attributes listed in the asssignemnt.
class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name,last_name,treats,pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# Implement walk(), feed(), bathe() on the ninja class.
# implement the following methods:

# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f'{self.first_name} {self.last_name} is walking {self.pet.name}.')
        self.pet.play()
        return self

# feed() - feeds the ninja's pet pet food invoking the pet eat() method
    def feed(self):
        print(f'{self.first_name} {self.last_name} is feeding {self.pet_food} to {self.pet.name}.')
        self.pet.eat()
        return self
    
# treat() - feeds the ninja's pet pet treat invoking the pet eat() method
    def treat(self):
        print(f'{self.first_name} {self.last_name} is feeding {self.treats} to {self.pet.name}.')
        self.pet.eat()
        return self
    
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f'{self.first_name} {self.last_name} is cleaning {self.pet.name}.')
        self.pet.noise()
        return self