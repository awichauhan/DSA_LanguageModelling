myText = "Hello"

encoded_bytes = myText.encode("utf-8")  #this will represent b'Hello'
print(encoded_bytes)

encoded = list(myText.encode("utf=8"))   # to see numerical value of each character
print(encoded)

decoded = bytes(encoded).decode("utf-8")
print(decoded)