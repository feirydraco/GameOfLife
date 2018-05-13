import binascii
str = "name"
binaryarr = []
for char in str:
    binaryarr.append(bin(ord(char))[2:])

print(binaryarr)
