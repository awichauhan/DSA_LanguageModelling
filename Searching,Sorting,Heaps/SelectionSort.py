arr = [111,333,33,99,6,1000,66,88,2,3,44,4000]


for i in range(len(arr)):
    min = i
    for j in range(i,len(arr)):
        if arr[min] > arr[j]:
            temp = arr[min]
            arr[min] = arr[j]
            arr[j] = temp

print(arr)




