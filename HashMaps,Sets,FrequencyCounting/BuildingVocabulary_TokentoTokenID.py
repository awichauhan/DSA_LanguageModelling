tokens = ["Hello", "My", "Name", "is", "Awantika"]
print("Tokens are: " ,tokens)
tokenIDs = []

for i in tokens:
    encoded = i.encode("utf-8")
    token_id = int.from_bytes(encoded, "big")
    tokenIDs.append(token_id)


print("Token IDs are: ", tokenIDs)

vocabulary = {}

for i in range(len(tokens)):
    vocabulary[tokens[i]] = tokenIDs[i]

print("Token to TokenID Vocab is: ", vocabulary)





