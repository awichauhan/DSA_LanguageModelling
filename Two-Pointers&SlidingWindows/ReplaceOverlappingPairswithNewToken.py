tokens = tokens = [1, 1, 1, 1]
a = 1
b = 1
x = 5

resultTokens = []
i = 0
while i < len(tokens):
    if tokens[i] == a and tokens[i + 1] == b:
        tokens[i] = x
        resultTokens.append(x)
        i += 2

    else:
        resultTokens.append(tokens[i])
        i+=1

print(resultTokens)