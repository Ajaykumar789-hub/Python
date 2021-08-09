#below script remove duplicates from list
ls=[1,2,3,5,2,6,3,2,7]

res=[]
for i in ls:
    if i not in res:
        res.append(i)

print(str(res))