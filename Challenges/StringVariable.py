#Assign a string to a variable

pig1 = "Hello! I have three pigs."

#assign a multiline string to a variable 3 double quotes

favquote = """ Agriculture is our wisest pursuit,
because it will in the end contribute most to 
real wealth, good morals, and hapiness. - Thomas Jefferson """

#return a range of characters by using the slice syntax

X = slice(0,10)
print(favquote[X])

#Use len()
print(len(pig1))
#Use strip()

#Use Upper()
Z = pig1.upper()
print(Z)

pig2 = " One piglet. They're names are Ruby, Cowboy, and Lily."

# Use the In keyword #Use the not in Keyword
print("pigs" in pig2)
if "two" in pig2:
    print("Yes, 'two' is present")

print("ruby" not in pig1)
if "Ruby" not in pig1:
    print("No, 'Ruby' is NOT present")




#concatenate a string 

#Concatenate a string

pigs = pig1 + pig2
print(pigs)

#use an escape character 

quoteHMC =" \"I feel ill,\"  Howl annouced. \"I'm going to bed, where I may die.\" - Howl's Moving Castle"
print(quoteHMC)