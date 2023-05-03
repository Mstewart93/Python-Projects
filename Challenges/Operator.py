#Complete these actions:
#Use an assignment operator.
#Use a comparison operator.
#Use a logical operator.
#Use an identity operator.
#Use a membership operator.
#Use a bitwise operator.

#Arithmatic

print(5 + 2)
print(7 - 2)
print(5 * 2)
print(62 / 2)
print(12 % 5) #returns the remainder
print(2 ** 4) #exponent
print(10 // 3) #will round the result to the nearest whole number

#Assignment opperator
z = 2
b = 2
c = 3
d = 2
e = 2
f = 2
g = 2
h = 2
i = 2
j = 2
k = 2
l = 2
m = 2

z = 5 #x=5
b += 3 #x = x+3
c -= 3 #x = x-3
d *=3 #X=X*3
e/=3 #x= x/3
f%=3 #x = X%3
g//=3 #x = x//3
h**=3 #x = X **3
i&=3 #x=   X&3
j |= 3 #X = X|3
k ^=3 #x = X^3
l>>=3 #x = X >> 3
m<<=3 #x= X << 3

#Comparison Operator

print(f == e ) #equals
print(f!=c) #not equals
print(c > f) #greater than
print(f < c) #less than
print(c >= f) #greater than or equal to
print(f <= c) #less than or equal to 


#logical operator

print(f < 5 and f > 1) #both have to be true
print(f < 5 or f < 1) #Only one has to be true
print(not(f<5 and f > 1)) #reverses the result true = false

#identity operator

print(j is i) #true if they are both the same 
print(j is not c) #true if they are different

#membership operator

num1 = 345678

print('4' in num1) #true if it is in it
print('1' not in num1) #true if it is not in it

#use bitwiseto compare ninary numbers
print(x & y) #AND sets each bit to 1 if both are 1
print(x|y) #OR sets each bit to 1 if one of them is 1
print(X^y) #XOR sets each bit to 1 if ONLY one of thm is one
print(~x) #NOT inverst all the bits
print(x<<2) #Zero fill left shift pushing zeros in from the right and let the leftmost fall off
print(X>>2) #Signed right shift push copies of the leftmost bit in fromt hte left and let the rightmost bits fall off. 

