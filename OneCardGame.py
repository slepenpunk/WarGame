import random


class Card:
    """One game card"""

    RANKS = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    SUITS = ['♠', '♥', '♦', '♣']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        res = f'{self.rank}{self.suit}'
        return res


class Hand:
    """Players hand"""

    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        if self.cards:
            res = ''
            for card in self.cards:
                res += str(card)
        else:
            res = '<empty>'
        return res

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)

    def clear(self):
        self.cards = []


class Deck(Hand):
    """Gaming deck"""

    def populate(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_card=1):
        for rounds in range(per_card):
            for hand in hands:
                top_card = self.cards[0]
                self.give(top_card, hand)


if __name__ == '__main__':
    ...

