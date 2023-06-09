#Python on VS Code
#Author:MeLyssa Stewart
# Purpose : Does aspart of a study during tech academy to apply different concepts.

#basic example
#def start():
#   print("Hello {}".format(get_name())) #wildcard squiggly will input variable when done with .format get name function we create format subs in variable
#def get_name():
#    name = input("What is your name?")
#return name
#if __name__== "__main__": 
#     start() #more complicated example
def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_name(f_name,l_name,age,gender) # order maters this will be order inputed in the placeholder
def get_name (f_name, l_name,age,gender) :
    print("My name is {} {}. I am a {} years old {}.".format(f_name,l_name,age,gender))


if __name__ == "__main__":
    start()