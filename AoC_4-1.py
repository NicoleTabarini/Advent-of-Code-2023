with open('input.txt', 'r') as file:
    lines = file.readlines()

winning_cards = []

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
            print(winning, card)
            count += 1

    print("count",count)
    if count > 0:
        print(2 ** (count-1))
        winning_cards.append(2 ** (count-1))
    
print(sum(winning_cards))
