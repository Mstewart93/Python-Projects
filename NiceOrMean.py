def start(nice=0,mean=0,name=""): #controls not getting error
    #get user's name
    name = describe_game(name) #passes name into the function
    nice,mean,name = nice_mean(nice,mean,name) # 3 variables with a new fuction that passes the variables into the functions

def describe_game(name):
    #check first to see if it is a new game or not
    #if its new get the name
    #if its not new thank the player for playing again and continue 
    if name  != "":
        print("\n Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\n What is your name? \n>>>>").capitalize()
                if name != "":
                    print("\n Welcome, {} !".format(name))
                    print("\n In this game, you will be greeted\n by several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name # returns it into the name variable

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\n A stranger approaches you for a \nconversation. Will you be nice\n or mean? (N/M) \n>>>>").lower()
        if pick == "n":
            print("\n The stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\n The stranger glares at you \n menacingly and stomps off...")
            mean = (mean + 1)
            stop = False
        if pick == "k":
            print("The child smiles at you, then runs off to her parents...")
            nice = (nice +1)
            stop = False
        if pick == "r":
            print("The child bursts into tears, her parents glaring at you as they come to comfort her...")
            mean = (mean +1)
            stop = False
    score(nice,mean,name) #passes the 3 variable t0 the score

def show_score(nice,mean,name):
    print("\n{}, your current total: \n ({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name) :
    #this is a fuction that passess the values stored in the variables
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice, mean, name):
    print("\n Nice Job {}, you win! \n Everyone loves you and you've \n made lots of friends along the way!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\n Ahhh too bad, game over! \n {}, you live in a dirty beat up \n Van by the river, wretched and alone!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True 
    while stop:
        choice = input("\n Do you want to play again? (y/n): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\n Oh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\n Enter ( Y ) for 'Yes', ( N ) for 'No' : \n >>>")


def reset(nice,mean,name): 
    nice = 0
    mean = 0 
    start(nice,mean,name) # we are not reseting name as we already know it, and they already know how to play.



if __name__ == "__main__":
        start()
