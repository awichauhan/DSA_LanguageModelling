arr = [111,333,33,99,6,1000,66,88,2,3,44,4000]

count = len(arr) -1

while count != 0:
    for j in range(0,count):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    count-=1



print(arr)
