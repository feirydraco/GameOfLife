x = "some string"

def convertGOL(data):
    b_a = []
    for _ in data:
        b_a.append(bin(ord(_)))
    actual_data = []
    for _ in b_a:
        actual_data.append(int(_[2:]))
    print(actual_data)
    for row in actual_data:
        for bit in str(row):
            print(str(bit) + str(" "), end = "")
        print(end="\n")
convertGOL("p")
