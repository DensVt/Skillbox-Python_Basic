from test import Deck, Player

BJ_deck = Deck()
BJ_deck.shuffle()

player_1 = Player('Бот')
player_2 = Player('Игрок')

player_1.own_cards = []
player_2.own_cards = []

player_1.own_cards.append(BJ_deck.cards.pop())
player_1.own_cards.append(BJ_deck.cards.pop())
player_1.own_cards_info()
player_1.cards_count_info()
player_2.own_cards.append(BJ_deck.cards.pop())
player_2.own_cards.append(BJ_deck.cards.pop())
player_2.own_cards_info()
player_2.cards_count_info()


while True:
    flag_1 = True
    if flag_1:
        ask_for_player_1 = input(f'{player_1.name}, еще карту? (y/n) ')

        if ask_for_player_1 == 'n':
            player_1.cards_count_info()
            flag_1 = False
            break
        elif ask_for_player_1 == 'y':
            player_1.own_cards.append(BJ_deck.cards.pop())
            player_1.own_cards_info()
            player_1.cards_count_info()

            if player_1.cards_count() == 21:
                player_1.score_up()
                print(f'В этом раунде победил {player_1.name}!\n')
                break
            elif player_1.cards_count() > 21:
                player_2.score_up()
                print(f'В этом раунде победил {player_2.name}!\n')
                break
            elif player_2.cards_count() == player_1.cards_count():
                print(f'В этом раунде победила дружба!')
                break

while True:

    if player_1.cards_count() >= 21:
        break
    else:
        ask_for_player_2 = input(f'{player_2.name}, еще карту? (y/n) ')
        if ask_for_player_2 == 'n':
            player_2.cards_count_info()
            # player_2.cards_count()
            break
        elif ask_for_player_2 == 'y':
            player_2.own_cards.append(BJ_deck.cards.pop())
            player_2.own_cards_info()
            player_2.cards_count_info()

            if player_2.cards_count() == 21:
                player_2.score_up()
                print(f'В этом раунде победил {player_2.name}!\n')
                break
            elif player_2.cards_count() > 21:
                player_1.score_up()
                print(f'В этом раунде победил {player_1.name}!\n')
                break
            elif player_2.cards_count() == player_1.cards_count():
                print(f'В этом раунде победила дружба!')
                break

if player_2.cards_count() == player_1.cards_count():
    print(f'В этом раунде победила дружба!')
    # break
elif 21 >= player_2.cards_count() > player_1.cards_count():
    print(f'В этом раунде победил {player_2.name}!')
    # break
elif 21 >= player_1.cards_count() > player_2.cards_count():
    print(f'В этом раунде победил {player_1.name}!')
    # break



