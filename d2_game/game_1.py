games = open('games data.txt', "r").read().split("\n")
game_id_sum = 0
limit_R = 12
limit_G = 13
limit_B = 14


def get_id(game):
    return game.replace('Game ', '').split(': ')[0]


def is_game_legal(game):
    sets = game.split(': ')[1].split('; ')
    for set in sets:
        if not is_set_legal(set):
            return False
    return True


def is_set_legal(set):
    pairs = set.split(', ')
    for pair in pairs:
        if is_above_limit(pair):
            return False
    return True


def is_above_limit(pair):
    amount = int(pair.split(' ')[0])
    colour = pair.split(' ')[1]
    if amount > limit_B:
        return True
    elif colour == 'red':
        return amount > limit_R
    elif colour == 'green':
        return amount > limit_G
    elif colour == 'blue':
        return amount > limit_B


for game in games:
    if is_game_legal(game):
        game_id_sum += int(get_id(game))

print(game_id_sum)
