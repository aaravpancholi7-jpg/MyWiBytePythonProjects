import csv
import random

def display_card(card):
    max_chars = 0
    for keys in card:
        if len(keys)>max_chars:
            max_chars = len(keys)

    for keys in card:
        print(keys, (max_chars-len(keys))*' ', ': ', card[keys])

def determine_winner(m1, m2, order = 1):
    dct = {'player': m1, 'computer': m2}
    v = list(dct.values())
    k = list(dct.keys())

    if m1 == m2:
        return 'draw'
    else:
        if order == 1:
            return k[v.index(max(v))]
        else:
            return k[v.index(min(v))]

def training():
    display_best_card()
    print()
    print('More training ...')
    n = 4
    for k in relevant_keys:
        print()
        print('Top ', n, ' card for ', k)
        display_top_cards(k,n)
        input()


def display_top_cards(category, n):


    if inv_mapping_dict[category] in ['H', 'F', 'B']:
        all_cards_s = sorted(all_cards, key = lambda x : float(x[category]), reverse = True)
    else:
        all_cards_s = sorted(all_cards, key = lambda x : float(x[category]))

    keys = list(all_cards_s[0].keys())
    keys_len = [len(key) for key in keys]

    longest_val = []

    for k in keys:
        all_cards_d = sorted(all_cards, key = lambda x : len(x[k]))
        longest_val.append(len(all_cards_d[-1][k]))



    max_col = zip(keys_len, longest_val)
    max_col = [max(m) for m in max_col]

    for k in all_cards_s[0]:
        print(k, end = '')
        print((max_col[keys.index(k)]- len(k))*' ', end = '|')
    print()

    for card in all_cards_s[0:n:]:
        for k in card:
            print(card[k], end = '')
            print((max_col[keys.index(k)]- len(card[k]))*' ', end = '|')
        print()



def display_best_card():
    print("I will tell you the best card for each category")

    for kk in relevant_keys:
        all_cards_s = sorted(all_cards, key = lambda x : float(x[kk]))

        if inv_mapping_dict[kk] in ['H', 'F', 'B']:
            best_card = all_cards_s[-1]
        else:
            best_card = all_cards_s[0]

        print()
        print('The best card for category ', kk)
        display_card(best_card)
        input()




print('Welcome to the Top Trumps Game, Skyscrapers theme')
print('Maky your choices wisely and try to win all the cards')
print('Click Enter to begin')

input()


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
inv_mapping_dict = {}

for key in relevant_keys:
    mapping_dict[key[0]] = key
    inv_mapping_dict[key] = key[0]



chance = 'player'


game_over = False

training_needed = input('Would you like to have a short training?(Y/N)')

if training_needed == 'Y':
    training()



while not game_over:

    input()

    print('player cards: ', len(player_cards), 'computer cards: ', len(comput_cards), 'table cards: ', len(table_cards))
    player = player_cards.pop(0)
    comput = comput_cards.pop(0)
    table_cards.append(player)
    table_cards.append(comput)

    print()
    print('It is ', chance + '\'s', ' chance now')
    print()
    print('Your (player card) is:')
    display_card(player)

    print()


    if chance == 'player':
        chosen_key = input('What is your choice (H/F/Y/B/T)?')
        chance = 'computer'
    elif chance == 'computer':
        chosen_key = random.choice(list(mapping_dict.keys()))
        chance = 'player'


    key_requested = mapping_dict[chosen_key]
    value_player = player[key_requested]
    value_comput = comput[key_requested]

    print('Key requested is ', key_requested)
    print('Player ', key_requested, ' is ', value_player)
    print('Computer ', key_requested, ' is ', value_comput)

    if chosen_key in ['H', 'F', 'B']:
        winner = determine_winner(float(value_player), float(value_comput))
    else:
        winner = determine_winner(float(value_player), float(value_comput), 0)

    print('Winner is ', winner)

    if winner == 'player':
        player_cards.extend(table_cards)
        table_cards.clear()
    elif winner == 'computer':
        comput_cards.extend(table_cards)
        table_cards.clear()

    if len(player_cards) == 0:
        print('The computer won the game')
        game_over = True
    elif len(comput_cards) == 0:
        print('The player won the game')
        game_over = True