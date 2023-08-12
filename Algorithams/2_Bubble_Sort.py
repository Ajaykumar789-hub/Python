def bubbleSort(arr):
    for start in range(len(arr)):
        for i in range(len(arr)-1,start,-1):
            if (arr[i-1] > arr[i]):
                (arr[i-1],arr[i]) =(arr[i],arr[i-1])
    
    return arr

arr = [6,10,8,4,6,3,1]

print(bubbleSort(arr))