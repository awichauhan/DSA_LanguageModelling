tokens = [10,20,30,88,22,20,10,55,88,77,33,40,40,22,100,40]

freq_table = {}
most_frequent = None
frequency = 0

for i in tokens: # need to iterate over values
    if i in freq_table:
        freq_table[i] +=1
    else:
        freq_table[i] = 1


for pair, freq in freq_table.items(): #to give key-value pair
    if freq > frequency:
        most_frequent = pair
        frequency = freq

print("Frequent pair is ", most_frequent)
print("Their frequency is ", frequency)


