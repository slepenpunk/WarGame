import OneCardGame, games, operator


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

    def __init__(self, names):
        self.players = []
        self.hands = []
        for name in names:
            player = Player(name, 0)
            self.hand = Hand()
            self.players.append(player)
            self.hands.append(self.hand)
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        max_score = {}
        winner_score = None
        winner_name = None
        self.deck.deal(self.hands)
        for player in self.players:
            card = self.hands.pop(0)
            player.score = card.total
            print(player.name, card)
            max_score[player.name] = player.score
            m_score = max(max_score.values())
            w_name = max(max_score, key=max_score.get)
            winner_score = m_score
            winner_name = w_name
        print(f'Winner - {winner_name}\n'
              f'Score - {winner_score}')

        # first_player = self.players[0]
        # second_player = self.players[1]
        # if first_player.score > second_player.score:
        #     first_player.win()
        #     second_player.lose()
        # if second_player.score > first_player.score:
        #     second_player.win()
        #     first_player.lose()
        # if first_player.score == second_player.score:
        #     print('Tie!')


def main():
    print(f'Welcome to game "War"!\n'
          f'Players draw one card and wins who has a highest card.')
    again = None
    while again != 'n':
        try:
            number = games.ask_number('How much players?(2-36): ')
            if number not in range(2, 37):
                raise IndexError
            players = []
            for i in range(number):
                name = input('Enter name: ')
                players.append(name)
            game = Game(players)
            game.play()
            again = games.ask_yes_no('Do you want play again?(y/n): ')
        except IndexError:
            print('Range of players - from 2 to 36!')


main()
