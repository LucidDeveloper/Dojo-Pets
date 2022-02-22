'''@ author
Gianni M. Javier
'''

# NINJA BONUS: Use modules to separate out the classes into different files.
# Module import format for Class import
# from <file_name> import <class_name>

from ninja import Ninja
from pets import Cat, Dog

# Make an instance of a Ninja 
# and assign them an instance of a pet to the pet attribute.
# Constructor for Ninja Class
# def __init__(self, first_name,last_name,treats,pet_food, pet):
# Constructor for Pet Class
# def __init__(self,name,type,tricks, energy = 100, health = 100):
# SENSEI BONUS: Use Inheritance to create sub classes of pets.
# Dog Class and Cat Class are Both Sub Classes of the Pet Class

male_ninja = Ninja('Gianni Manuel','Javier','Buffalo Bits','Beneful',Dog('Blue','Siberian Husky',['Sit', 'Fetch', 'Hih-five','Stand', 'Stay', 'Come', 'Roll-Over'],100,100))
female_ninja = Ninja('Andrea Eya','Avila','Meow Mix','Purina',Cat('Kitty','Siberian',['Sit', 'Fetch', 'High-five', 'Stand', 'Stay', 'Come', 'Roll-Over'],100,100))
child_ninja = Ninja('Patrick Antonius', 'Javier','Buffalo Bits', 'Beneful', Dog('Doggy','Shiba Inu',['Sit', 'Fetch', 'Hih-five','Stand', 'Stay', 'Come', 'Roll-Over'], 100, 100))

# Have the Ninja feed, walk , and bathe their pet.
male_ninja.feed().walk().treat().bathe()
female_ninja.feed().walk().treat().bathe()
child_ninja.feed().walk().treat().bathe()



