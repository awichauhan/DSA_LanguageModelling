tokens = [10, 20, 10, 20, 30, 10, 20]

tokenPair_frequencyTable = {}


for i in range(len(tokens) -1):
    pair = (tokens[i],tokens[i+1])

    if pair in tokenPair_frequencyTable:
        tokenPair_frequencyTable[pair] += 1
    else:
        tokenPair_frequencyTable[pair] = 1

print(tokenPair_frequencyTable)