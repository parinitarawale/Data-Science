fd = open ("data.txt", "r")
text = fd.read()
print(text)
#output -->Hello Everyone
fd.close()
