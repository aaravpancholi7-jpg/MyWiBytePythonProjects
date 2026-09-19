import csv
import random

def display_card(card):
    max_chars = 0
    for keys in card:
        if len(keys)>max_chars:
            max_chars = len(keys)

    for keys in card:
        print(keys, (max_chars-len(keys))*' ', ': ', card[keys])

with open('Top Trumps - Skyscrapers.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)

relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]

random.shuffle(all_cards)

comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []

mapping_dict = {}
for key in relevant_keys:
    mapping_dict[key[0]] = key

chance = 'player'


game_over = False

while not game_over:
    player = player_cards.pop(0)
    comput = comput_cards.pop(0)
    table_cards.append(player)
    table_cards.append(comput)


    print()
    print('Your card is ...')
    display_card(player)
    if chance == 'player':
        chosen_key = input('What is your choice?')
        chance = 'computer'
    else:
        chosen_key = random.choice(list(mapping_dict.keys()))

    key_requested = mapping_dict[chosen_key]
    value_player = player[key_requested]
    value_comput = comput[key_requested]
    print('Key interest is ', key_requested)