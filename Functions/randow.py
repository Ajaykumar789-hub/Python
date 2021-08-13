l=[]
f=open("Employeedata.txt","r")

f1=f.read().splitlines()
for x in f1:
    if x not in l:
        l.append(x)
with open('your_file.txt', 'w') as f:
    for item in l:
        f.write("%s\n" % item)