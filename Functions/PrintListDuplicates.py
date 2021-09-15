#print only duplicates from list

ls=[ 10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

x=[]
print(set([x for x in ls if ls.count(x) > 1]))