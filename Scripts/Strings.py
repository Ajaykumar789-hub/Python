#string in python surrounded by single quote or double quote

x="Ajay"

y="""This is Ajay
I live in Richmond VA"""

print(x)
print(y)

print(type(y))

# string are array of chars

print(x[0]) #output will be A

#this means we can loop string in python

x="Ajaykumar"
for c in x:
    print(c)  # run this to check output


x="ajay"

print("aj" in x) # in operator used to see certian keyword is there or not


#concate strings in python
x="ajay"
y="kumar"
z=x+" "+y
print(z)

#slices(substring) from string

name="ajayKumar"
print(name[1:5])

print(name[-3:-1]) #in revers order

print(name[:4])