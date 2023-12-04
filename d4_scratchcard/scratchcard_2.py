cards = open('pile of cards.txt', "r").read().split("\n")
scratchcards_instances = [0] * len(cards)


def copy(amount, index):
    for to_copy in range(scratchcards_instances[index]):
        for w in range(amount):
            scratchcards_instances[index + w + 1] += 1


for i, card in enumerate(cards):
    wins = 0
    scratchcards_instances[i] += 1
    card = card.replace('Game ', '').split(': ')[1].replace('  ', ' ')
    winning_numbers = card.split(' | ')[0].split(' ')
    chosen_numbers = card.split(' | ')[1].split(' ')
    for number in chosen_numbers:
        if number in winning_numbers:
            wins += 1
    if not wins == 0:
        copy(wins, i)


print(sum(scratchcards_instances))
