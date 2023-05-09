mySentenceHello = 'I love' #string

animal_list = ['Dogs','Pigs','Chickens','Horses','Goats','Cats'] #list

#we can concatenate the entire thing or we can just pick on item from the list. 

#lets define our function and do just that, the bellow will call the item in position zero we need to iteratce or cycle.

def animal_function():
    print ("{} {}".format(mySentenceHello, animal_list[0]))


animal_function()

def animal_function_all():
    for i in animal_list:    
        print ("{} {} {}".format(mySentenceHello, i))

animal_function_all()


