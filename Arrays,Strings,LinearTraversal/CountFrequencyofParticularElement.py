arr = [3,5,6,3,0,2,5,1,1,5,8,0,3,3,3,3,3,3]

targetElement = 3
freq = 0

for i in arr:
    if i == targetElement:
        freq +=1

print(freq)