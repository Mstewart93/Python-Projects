#assign a variable, and test the numbers 12, 15, and 10

num1 = 12
key =  False

if num1 == 12:
    if key :
         print("Num1 is equal to Twelve and they have the key!")
    else : 
        print("Num1 is equal to Twelve and they DO NOT have the key!")
elif num1 < 12:
    print("Num1 is less than  Twelve!")
else: 
    print("Num1 is NOT equal to Twelve!")

i = 0
for i in range(10) :
    print("{} iteration through the loop.".format(i))
    i += 1

while i < 10:
    print("{} iteration through the loop.".format(i))
    i += 1

name = 'MeLyssa'
print(len(name))
for i in enumerate(name):
    print(i)