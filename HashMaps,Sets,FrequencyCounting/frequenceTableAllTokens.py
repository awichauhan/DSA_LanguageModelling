tokens = [10,20,30,88,22,20,10,55,88,77,33,40,40,22,100]

freq_table = {}

for i in tokens: # need to iterate over values
    if i in freq_table:
        freq_table[i] +=1
    else:
        freq_table[i] = 1

print(freq_table)

