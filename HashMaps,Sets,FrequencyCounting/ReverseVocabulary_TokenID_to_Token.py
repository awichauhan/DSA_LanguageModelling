tokens = ["Hello", "My", "Name", "is", "Awantika"]
print(tokens)

tokenIDs = []
Vocab = {}
ReverseVocab = {}

for i in tokens:
    encoded = i.encode("utf-8")
    token = int.from_bytes(encoded)
    tokenIDs.append(token)

print(tokenIDs)

for i in range(len(tokens)):
    Vocab[tokens[i]] = tokenIDs[i]

print(Vocab)

for i in range(len(tokenIDs)):
    ReverseVocab[tokenIDs[i]] = tokens[i]

print(ReverseVocab)
