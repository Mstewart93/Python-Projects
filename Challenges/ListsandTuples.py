#TUPLE sequence of immutable objects which means that they cannot be changed. 
#LIST VS TUPLE
    #LIST can be changed uses []
    #TUPLE can NOT be changed uses ()

animal = ('Zebra', 'Aligator', 'Giraffe', 'Goat','Ox') #TUPLE

#we want to change the above so create a list from the tuple so it can be changed

listofanimals = list(animal)
print(listofanimals)

#to add we do :
listofanimals.append ("Honey Badger")
print(listofanimals)

# Create a list

petlist = ["Ruger", "Doc","Ruby", "Cowboy","Lily"]
pettype = ["dog", "pig", "chicken"]

#Loop through a list with a for loop

for x in petlist:
    print(x)

#use the append() method

petlist.append ("Nubs")
print(petlist)

#make a copy of a list. List method copy()

X = petlist.copy()

#concatenate two lists.

print(petlist + pettype)

#use the reverse() method list

print(petlist.reverse())




