#to performa some kind of operarion
#print(10+5) #addition operation
#  +,- * 

"""Arithematic operators"""
x=3 
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)#/ division
print(x%y)# % modulus
print(x**y)# ** exponention
print(x//y)# // floor division
"""Assignment operators: to assign values to variables"""
#x=3
#x+=3 or x=x+3 are same
"""Comparision Operators"""
#== equal
#!= not equal, >,< >=,<= 
# the output of comparsion operators is boolean
"""Logical operators"""
#to know x value 0 to 9 or not
x=6
if x>0 and x<9:
    print(x,"is between 0 to 9")
else:
    print(x," is less than 0")


x=6
if x<0 or x>9:
    print(x,"is not between 0 to 9")
else:
    print(x,"is between 0 to 9")
#

x=10
y=5
print(not(x>y and y<x))

""""Identity operators"""
# is used to compare objects not if they are equal
#if they are same object with the same memory location
x=["123","888"]
y=["hash","jans"]
z=x
print(id(x))
print(id(y))
print(id(z))

"""Membership operators"""
#used to test of a sequence is present or not in string, list, tupple or dict
x="Ajaykumar"
print("A" in x)

y=[1,2,3,4]
print(5 in y)
print(2 in y)
print(2 not in y)

"""Bitwise Operators"""
#&,|(or),^(xor) ~(not) <<,>>

print(bin(21))

x=20
y=5
print( x & y)  # only two bits are 1 then 1
print(x | y) #set each bit to 1 if one is 1
print(x ^ y) #only one of two bits is 1
print(~x) #inverts all bits formula (-x-1)

print(x << 2) #2 positions of x moved to left
print(x>>2) # 2 positions of x moved to right

