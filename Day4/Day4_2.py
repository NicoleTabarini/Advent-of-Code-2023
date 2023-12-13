with open('input.txt', 'r') as file:
    lines = file.readlines()

cards_dict = {key:1 for key in range(len(lines))}

c = 0

for line in lines:
    line = str(line)
    line = line.split(":")[1]
    winning = line.split("|")[0]
    cards = line.split("|")[1]
    winning = set(winning.split())
    cards = set(cards.split())

    count = 0

    for card in cards:
        if card in winning:
            count += 1
            
    if count != 0:
        for n in range(1,count+1):
            cards_dict[c + n] += cards_dict[c]

    c += 1


print(sum(cards_dict.values()))


# 0 - .
# 1 - ..
# 2 - ....
# 3 - ........
# 4 - ............
# 5 - ................
# 6 - ................
# 7 - ....
# 8 - ....
# 9 - ....
# 10 - ....
# 11 - ...
# 12 - .
# 13 - .
