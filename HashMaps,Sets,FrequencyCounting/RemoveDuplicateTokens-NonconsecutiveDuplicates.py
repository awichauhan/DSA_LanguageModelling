#Using optimized approach of hashSet and linear scan


tokens = [10, 20, 50 , 30, 10, 40, 20, 50]

nonDuplicateSet = set()
i = 0

for j in range(len(tokens)):
    if tokens[j] not in nonDuplicateSet:
        nonDuplicateSet.add(tokens[j])

        tokens[i] = tokens[j]
        i +=1

print(tokens[:i])