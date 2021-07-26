#variable contain/store data 
#in python variable are case sensitive
#python doesnot have any command to declare varible
#we can change data type any time in python
#e.g a=5     a="ajay"
#variables declare like a-z,0-9 or _
# eg _a is allowed in pyhton
a,b,c = "ajay","kumar","john" #assining multiple values to multple variable
print(a)
print(b)
print(c)
a=b=c="fruit"  #assigning same value to all variables
print(a)
print(b)
print(c)

"""There is two types of varibles
1.Local variable: variables which create inside function"""


def myfunc():
    x="ajay kumar" #variable x defined inside function myfunc()
    print(a)

myfunc()


"""2.Global variable:variables which declared outside function and can be used anywhere both inside and outside
"""

y="kumar" #global variable
def myfun():
    z="chanti" #local varible
    print(z)
    print(y)

myfun()
print(y)

#to create global variable inside function use global keyword

y="kumar"
def myfun1():
    global y
    y="name"

myfun1()
print(y) # output comes which written insde function