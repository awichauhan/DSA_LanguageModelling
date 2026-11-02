arr = [111,333,33,99,6,1000,66,88,2,3,44,4000]

for i in range(len(arr)-1):
    min = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min]:
            min = j
    if min != i:
        arr[i], arr[min] = arr[min], arr[i]

print(arr)



"""
MY APPROACH WAS RATHER SOMETHING LIKE EXCHANGE SORT:
for i in range(len(arr)):
    min = i
    for j in range(i,len(arr)):
        if arr[j] < arr[min]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

ISSUES:
- idea of selection sort is to remember where the smallest element is, and that tracking isn’t happening.
- swap inside the inner loop instead of once after it.

"""

