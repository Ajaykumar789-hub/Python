# to store multiple values
# lists are ordered, mutable and allow duplicated  values aswell
#it can have different types aswell
mylist=["apple",1,"cherry"]
print(mylist)

print(mylist[1]) #lists are are ordered we can access them by index numbers
print(len(mylist)) #to get lenght of list

print(mylist[-2])
print(mylist[0:2])

mylist[0]="banana"
print(mylist) #lists are mutable
mylist[0:2]=["apple","banana"]
print(mylist)

mylist.append("grapes") #to append to list

print(mylist)

mylist.insert(0,"pine apple")
print(mylist)

mylist.remove("pine apple")
print(mylist)