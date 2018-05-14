x = "some string"

#n = 0

#for char in x:
#    n += ord(char)
#print(n)


def convertGOL(data):
    b_a = []
    for _ in data:
        b_a.append(bin(ord(_)))
    actual_data = []
    for _ in b_a:
        actual_data.append(int(_[2:]))
    return actual_data


print(convertGOL("hello"))
