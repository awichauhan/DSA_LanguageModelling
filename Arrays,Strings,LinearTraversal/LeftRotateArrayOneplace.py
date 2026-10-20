arr = [2,3,4,5]

first = arr[0]
for i in range(1,len(arr)):  # we have to start the loop from 1 and not 0
    arr[i-1] = arr[i]

arr[len(arr) -1] = first

print(arr)

#time complexity = O(N)
#space complexity = O(N); using array in the algorithm
# space complexity of extra space is O(1)
