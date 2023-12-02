games = open('games data.txt', "r").read().split("\n")
game_power_sum = 0


def power_of_game(game):
    max = [0, 0, 0]
    sets = game.split(': ')[1].split('; ')
    for set in sets:
        max = get_max_set(set, max)
    return max[0] * max[1] * max[2]


def get_max_set(set, max):
    pairs = set.split(', ')
    for pair in pairs:
        max = get_max_pair(pair, max)
    return max


def get_max_pair(colour, max):
    amount = int(colour.split(' ')[0])
    colour = colour.split(' ')[1]
    if colour == 'red':
        if max[0] < amount:
            max[0] = amount
    elif colour == 'green':
        if max[1] < amount:
            max[1] = amount
    elif colour == 'blue':
        if max[2] < amount:
            max[2] = amount
    return max


for game in games:
    game_power_sum += int(power_of_game(game))

print(game_power_sum)
