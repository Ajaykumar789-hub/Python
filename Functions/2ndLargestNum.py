list=[10,20,6,78,9]
mx=max(list[0],list[1])
secondmax=min(list[0],list[1])
n=len(list)
for i in range(2,n):
    if list[i]>mx:
        secondmax=mx
        mx=list[i]
    elif list[i]>secondmax and mx != list[i]:
        secondmax=list[i]
print("2nd highest num is : ",str(secondmax))