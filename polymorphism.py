#Create two classes that inherit from another class.
#Each child should have at least two of their own attributes.
#The parent class should have at least one method (function).
#Both child classes should utilize polymorphism on the parent class method.
import random
class Sentiant: 
    #define attributes
    name = ""
    health_points = 0
    strength = 0
    level = 0 
    def newCharacter(self):
        entry_name  = (input("Enter your name: "))
        generate_health = random.randint(0,10)
        generate_strength = random.randint(0,10)
        level = 0
        if len(entry_name) < 20 and len(entry_name) > 0:
            print("Welcome! {}!".format(entry_name))    
        else:
            print("Error Name invalid please try again")

    
#otside of class create instance of the class

#def __init__ (self,name,health_points,strength,level):
    #self.name = name
    #self.health_points = health_points
    #self.strength = strength
    #self.level = level

#New_user =  Sentiant("Joe L.",10, 5, 1)

class Druid(Sentiant):
    Earth_Connection = 15
    animal_forms = 0
    level = 5

    def newCharacter(self):
        entry_name  = input("Enter your name: ")
        generate_health = random.randint(0,10)
        generate_strength = random.randint(0,10)
        generate_level = random.randint(0,10)
        if (generate_level == 5):
            print("Welcome esteemed Druid! {}!".format(entry_name))    
        elif (generate_level == 3):
            print("Welcome honored wizard {}!".format(entry_name))
        else: 
             print("Welcome! {}!".format(entry_name))

class Wizard(Sentiant):
    MP = 0
    Spell_size = 0
    level = 3 
    def newCharacter(self):
        entry_name  = input("Enter your name: ")
        generate_health = random.randint(0,10)
        generate_strength = random.randint(0,10)
        generate_level = random.randint(0,10)
        if (generate_level == 5):
            print("Welcome esteemed Druid! {}!".format(entry_name))    
        elif (generate_level == 3):
            print("Welcome honored wizard {}!".format(entry_name))
        else: 
             print("Welcome! {}!".format(entry_name))


user = Sentiant()
user.newCharacter()

druid1 = Druid()
druid1.newCharacter()

wizard1 = Wizard()
wizard1.newCharacter()