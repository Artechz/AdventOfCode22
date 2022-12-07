f = open("../data/day6.txt", "r")
contents = f.read()
print(contents, "\n")

SIZE_OF_PACKAGE = 14

for i in range(SIZE_OF_PACKAGE-1, len(contents)):
    valid_marker = 1
    for character in contents[i-(SIZE_OF_PACKAGE-1):i+1]:
        if contents[i-(SIZE_OF_PACKAGE-1):i+1].count(character) > 1:
            valid_marker = 0

    if valid_marker:
        print("marker '" + contents[i-(SIZE_OF_PACKAGE-1):i+1] + "' at position: ", i+1)
        print(contents[0:i-(SIZE_OF_PACKAGE-1)] + "".join([character.upper() for character in contents[i-(SIZE_OF_PACKAGE-1):i+1]]) + contents[i+1:len(contents)])
        for j in range(0, i-(SIZE_OF_PACKAGE-1)):
            print(" ", end="")
        for j in range(0, SIZE_OF_PACKAGE):
            print("^", end="")
        break
