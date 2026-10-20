
# Linear Search
arr = [4,5,8,9]
target = 2
count = 0
flag = 0

for i in range(0,len(arr), 1):  # i stores index value as we have given range of array
    count = count + 1
    if arr[i] == target:
        flag += 1
        print("Target exists at ", count)

if flag == 0:
    print("Target doesnt exist")

# Linear Scan (finding

arr1 = [8,2,3,5, 77, 11]
max = arr1[0]
min = arr[0]

for i in arr1:  # i stores the value of array so we can directly 
    if i > max:
        max = i
    elif i < min:
        min = i
print(max)
print(min)


