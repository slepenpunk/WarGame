import random


class Card:
    '''Create one game card'''
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♠', '♥', '♦', '♣']

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def __str__(self):
        if self.face_up:
            res = self.rank + self.suit
        else:
            res = 'XX'
        return res

    def flip(self):
        self.face_up = not self.face_up

class Hand(object):
    '''Players hand'''

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            res = ''
            for card in self.cards:
                res += str(card) + '\t'
        else:
            res = '<empty>'
        return res

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """Gaming deck"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def deal(self, hands, per_card=1):
        for rounds in range(per_card):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('No cards!')

    def shuffle(self):
        random.shuffle(self.cards)


if __name__ == '__main__':
    print('This module for a card games.')