arr = [111,333,33,99,6,1000,66,88,2,3,44,4000]


for i in range(len(arr)-1):
    j=i
    while j > 0:
        if arr[j] < arr[j-1]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
        j-=1

print(arr)
