cards = open('pile of cards.txt', "r").read().split("\n")
points = 0


for card in cards:
    counter = 0
    card = card.replace('Game ', '').split(': ')[1].replace('  ', ' ')
    winning_numbers = card.split(' | ')[0].split(' ')
    chosen_numbers = card.split(' | ')[1].split(' ')
    for number in chosen_numbers:
        if number in winning_numbers:
            counter += 1
    if counter > 0:
        points += 2 ** (counter - 1)


print(points)
