f = open("../data/day5_test.txt", "r")
contents, instructions = f.read().split("\n\n")
print(contents)

num_of_stacks = int((contents.splitlines()[-1])[len(contents.splitlines()[-1]) - 1])
contents = contents.splitlines()[:-1][::-1]
print("num_of_stacks: ", num_of_stacks)
print("num_of_levels: ", len(contents))

cargo = []
for content in contents:
    cargo.append(content[1::4])

stacks = []
for i in range(0, num_of_stacks):
    stacks.append([])

for i in range(0, len(cargo)):
    for j in range(0, len(cargo[i])):
        if cargo[i][j] != " ":
            stacks[j].append(cargo[i][j])

instructions = [instruction.split(" ")[1:6:2] for instruction in instructions.splitlines()]

QUANTITY = 0
SOURCE = 1
DESTINATION = 2

# part one
for instruction in instructions:
    for i in range(0, int(instruction[QUANTITY])):
        stacks[int(instruction[DESTINATION][0]) - 1].append(stacks[int(instruction[SOURCE][0]) - 1].pop())
        print("\t\'" + stacks[int(instruction[DESTINATION][0]) - 1][len(stacks[int(instruction[DESTINATION][0]) - 1]) - 1] + "\': " + instruction[SOURCE] + " -> " + instruction[DESTINATION])

# part two
aux_stack = []
for instruction in instructions:
    for i in range(0, int(instruction[QUANTITY])):
        aux_stack.append(stacks[int(instruction[SOURCE][0]) - 1].pop())
    moved_items = len(aux_stack)
    for i in range(0, moved_items):
        stacks[int(instruction[DESTINATION][0]) - 1].append(aux_stack.pop())
        print("\t\'" + stacks[int(instruction[DESTINATION][0]) - 1][len(stacks[int(instruction[DESTINATION][0]) - 1]) - 1] + "\': " + instruction[SOURCE] + " -> " + instruction[DESTINATION])

print("RESULT: ")
print("\t", end="")
for stack in stacks:
    print(stack[len(stack)-1], end="")
