AnimalDict = {
    "Ruger" : "Dog",
    "Doc" : "Dog",
    "Lily" : "Pig",
    "Ruby" : "Pig",
    "Cowboy" : "Pig",

}

print(AnimalDict)

# use the get method

a = AnimalDict.get("Lily")
print(a)

#Change a value in the dictionary

AnimalDict["Lily"] = "piglet"
print(AnimalDict)

#add to the dictionary

AnimalDict["Nubs"] = "Chicken"
print(AnimalDict)
#create nested dictionary
MyDogsDict = {
    "Doc" : {
        "Age" : "3",
        "Color" : "Tri",
        "Breed" : "Mini Aussie",
    },
    "Ruger" : {
        "Age" : "9",
        "Color" : "White",
        "Breed" : "Labrador",
    }
}

print(MyDogsDict.get("Ruger"))

#from keys

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)

print(thisdict)