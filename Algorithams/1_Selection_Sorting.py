def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for inside in range(i, len(arr)):
            if arr[inside]<arr[min]:
                min = inside
        (arr[i],arr[min]) = (arr[min],arr[i])
    return arr

arr =[4,6,7,9,1,3,2]

print(selection_sort(arr))