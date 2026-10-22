arr = [10,20,30,40,50,60,70,110,140,190]

target = 45
flag = 0

if len(arr) % 2 == 0:
    mid = len(arr) /2
else:
    mid = (len(arr)+1) /2

if arr[int(mid)] > target:
    for i in range(0,int(mid)):
        if arr[i] == target:
            flag = 1
            print("target is found in first half")

else:
    for i in range(int(mid),len(arr)):
        if arr[i] == target:
            flag = 1
            print("target is found in second half")

if flag == 0:
    print("target not found")



