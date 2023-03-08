import OneCardGame, games


class Player(games.Player):
    """Player of game"""

    def win(self):
        print(self.name, 'win!')

    def lose(self):
        print(self.name, 'lose!')

    def tie(self):
        print('Tie!')


class Card(OneCardGame.Card):
    """One game card"""

    @property
    def value(self):
        val = 0
        card = 0
        if self.rank == 'A':
            card = 14
        if self.rank == 'K':
            card = 13
        if self.rank == 'Q':
            card = 12
        if self.rank == 'J':
            card = 11
        if type(self.rank) == int:
            card = self.rank
        val += card
        return val


class Hand(OneCardGame.Hand):
    """Players hand"""

    @property
    def total(self):
        for card in self.cards:
            return card.value


class Deck(OneCardGame.Deck):
    """Gaming deck"""

    def populate(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.add(Card(rank, suit))


class Game:
    """Main process of the game"""

    scores = []

    def __init__(self, names):
        self.players = []
        self.hands = []


        for name in names:
            self.player = Player(name, 0)
            self.hand = Hand()
            self.players.append(self.player)
            self.hands.append(self.hand)
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        print(self.deck)
        self.deck.deal(self.hands)
        print(self.deck)
        for player in self.players:
            card = self.hands.pop(0)
            player.score = card.total
            print(player, card)
        if self.players[0].score > self.players[1].score:
            self.player.win()
        else:
            self.player.lose()



def main():
    game = Game(['1', '2'])
    game.play()


main()
