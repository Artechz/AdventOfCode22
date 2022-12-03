def points(char1: str, char2: str):
    score = (ord(char2) - ord('W'))
    other = (ord(char1) - ord('A') + 1)
    print(str(other) + ", " + str(score))
    sub = other - score

    if (sub == -2 or sub == 1):
        return 0 + score
    if (sub == 2 or sub == -1):
        return 6 + score
    return 3 + score

    # score - other
    # draw = 0
    # win
    # rock - scissors = 1-3 = -2
    # paper - rock = 2-1 = 1
    # scissors - paper = 3-2 = 1
    # lost
    # s - r = 3-1 = 2
    # r - p = 1-2 = -1
    # p - s = 2-3 = -1


def points2(char1:str, char2:str):
    result = (ord(char2) - ord('X')) * 3
    other = (ord(char1) - ord('A') + 1)
    #print(result)
    if (result == 3):
        return other + result
    if (result == 0):
        return 0 + (other - 2) % 3 + 1
    if (result == 6):
        return result + (other % 3) + 1


f = open("../data/day2.txt", "r")
total = 0
contents = f.read().split("\n")
for game in contents:
    game = game.split(" ")
    print(game)
    total += points2(game[0], game[1])

print(total)
