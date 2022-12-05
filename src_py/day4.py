f = open("../data/day4.txt", "r")
contents = f.read().split("\n")

total_full_overlaps = 0
total_partial_overlaps = 0
for group in contents:
    pair = group.split(",")
    print(pair)
    elf1 = pair[0].split("-")
    elf2 = pair[1].split("-")
    print(elf1)
    print(elf2)
    # solution for part two
    if ((int(elf1[0]) <= int(elf2[0])) and (int(elf1[1]) >= int(elf2[1]))):
        print("range contained in")
        total_full_overlaps += 1
    elif ((int(elf1[0]) >= int(elf2[0])) and (int(elf1[1]) <= int(elf2[1]))):
        print("range contained in")
        total_full_overlaps += 1
    # solution for part one
    if ((int(elf1[0]) <= int(elf2[1])) and (int(elf1[0]) >= int(elf2[0]))):
         print("range contained in")
         total_partial_overlaps += 1
    elif ((int(elf1[0]) <= int(elf2[0])) and (int(elf1[1]) >= int(elf2[0]))):
         print("range contained in")
         total_partial_overlaps += 1


print("full overlaps: ", total_full_overlaps)
print("partial overlaps: ", total_partial_overlaps)
