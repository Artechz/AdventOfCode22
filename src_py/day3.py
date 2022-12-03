f = open("../data/day3.txt", "r")
contents = f.read().split("\n")

# solution for part one
total_priority = 0
for elf in contents:
    repeated_token = "";
    rucksack_1 = slice(0, len(elf) // 2)
    rucksack_2 = slice(len(elf) // 2, len(elf))
    for char1 in elf[rucksack_1]:
        for char2 in elf[rucksack_2]:
            if char1 == char2:
                repeated_token = char1
    #print(elf[rucksack_1], elf[rucksack_2])
    #print(repeated_token, " - ", ord(repeated_token) - ord("a")+1 if repeated_token >= 'a' else ord(repeated_token) - ord("A")+1+26)
    total_priority += ord(repeated_token) - ord("a") + 1 if repeated_token >= 'a' else ord(repeated_token) - ord("A") + 1 + 26
#print(total_priority)

# solution for part two
total_priority = 0
tmp = [contents[n:n+3] for n in range(0, len(contents), 3)]
for elf_group in tmp:
    repeated_token = ""
    for char1 in elf_group[0]:
        for char2 in elf_group[1]:
            if char1 == char2:
                for char3 in elf_group[2]:
                    if char1 == char3:
                        repeated_token = char1
    total_priority += ord(repeated_token) - ord("a") + 1 if repeated_token >= 'a' else ord(repeated_token) - ord("A") + 1 + 26
    print(elf_group)
    print(repeated_token)
print(total_priority)