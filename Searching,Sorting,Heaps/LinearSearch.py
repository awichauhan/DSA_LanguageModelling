arr = [4,8,7,0,9]
target = 2
flag = 0

for i in arr:
    if i == target:
        flag =1
        print("2 is found")
        break

if flag != 1:
    print("target does not exist")


