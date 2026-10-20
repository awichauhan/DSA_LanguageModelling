tokens = [10, 10, 20, 20, 20, 30, 25, 25, 50, 50, 50, 100, 120, 9]
"""
2-pointer solves the duplicates that exist consecutively (identical elements grouped together
 but not not all duplicates in an arbitrary unsorted array.
It cannot solve following input: 
tokens = [10, 20, 30, 10, 40, 20, 50]
"""

i = 0
for j in range(1, len(tokens)):
    if tokens[i] != tokens[j]:
        i =  i + 1
        tokens[i] = tokens[j]
k = i +1

print(tokens[:k])  #this is the key to print only unique elements

