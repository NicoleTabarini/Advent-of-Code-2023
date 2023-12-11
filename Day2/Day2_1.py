
max_red = 12
max_green = 13
max_blue = 14


with open('Day2/input.txt', 'r') as file:
    lines = file.readlines()

games = {}
possible_games = []

for line in lines:
    colon = line.index(":")
    game = line[5:colon]
    games[game] = {"red" : 0, "blue" : 0, "green" : 0}
    
    draws = line[colon+2:-1].split(";")
    
    colors = []

    for draw in draws:
        single = draw.split(",")
        for i in single:
            color = tuple(i.split())
            colors.append(color)

    for el in colors:
        if int(el[0]) > games[game][el[1]]:
            games[game][el[1]] = int(el[0])

for game in games:
    if games[game]["red"] <= max_red and games[game]["blue"] <= max_blue and games[game]["green"] <= max_green:
        possible_games.append(int(game))

print(sum(possible_games))
    