"""
Input (x): All token IDs except the last.
Target (y): All token IDs except the first.
"""

arr = [10,20,30,50,60]

x = []
y = []

for i in range(len(arr) -1):
    x.append(arr[i])
    y.append(arr[i+1])

print("Input sequence using indexing ", x)
print("Target sequence is ", y)

#Using python built in

tokens = [77,88,44,66,22,11]

input_sequence = tokens[: -1]
target_sequence = tokens[1:]

print("Input sequence using python array slicing ", input_sequence)
print("Target sequence using python array slicing", target_sequence)


