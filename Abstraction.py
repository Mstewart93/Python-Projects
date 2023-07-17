#Your class should contain at least one abstract method and one regular method.  
#Create a child class that defines the implementation of its parents abstract method.
#Create an object that utilizes both the parent and child methods.
 
from abc import ABC, abstractclassmethod

class Sorcerer(ABC):
    def spellCost(self, amount):
        print("Your Level 1 cure will cost you: ", amount)
    @abstractmethod 
    def mp (self amount):
        pass

class check(Sorcerer):
    def mp (self, amount):
        print('Your currently available MP is bellow '.format(amount) ', we are terribly sorry')

obj = check()
obj.spellcost("10 mp")
obj.mp("10 gp")

    