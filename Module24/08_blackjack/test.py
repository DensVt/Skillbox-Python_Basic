import random


class Card:
    suits = ['Пики', 'Трефы', 'Бубны', 'Черви']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Туз', 'Дама', 'Король']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_info(self):
        print(self.rank + ' : ' + self.suit)


class Deck:
    def __init__(self):
        self.cards = [(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deck_info(self):
        for card in self.cards:
            print(card[0] + ' : ' + card[1])


class Player:
    score = 0

    def __init__(self, name):
        self.name = name
        self.own_cards = []
        self.score = 0

    def player_info(self):
        print(f'{self.name}: побед - {self.score}')

    def own_cards_info(self):
        print(f'\nУ {self.name} (а) на руках: ')
        for own_card in self.own_cards:
            print(own_card[0] + ' : ' + own_card[1])

    def cards_count(self):
        count = 0
        for own_card in self.own_cards:
            if not own_card[1].isdigit():
                if own_card[1] == 'Туз' and count < 10:
                    count += 11
                elif own_card[1] == 'Туз' and count > 10:
                    count += 1
                else:
                    count += 10
            else:
                count += int(own_card[1])
        return count

    def cards_count_info(self):
        print(f'Количество очков у {self.name} (а) равно {self.cards_count()}\n')

    def score_up(self):
        self.score += 1
        print(f'{self.name} выиграл!')