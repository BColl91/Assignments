import Cards, Games

class HighCard(Cards.Card):
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        super().__init__(rank, suit)

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    @property
    def value(self):
        return HighCard.ranks.index(self.rank)


import Cards, Games

class HighCard(Cards.Card):
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, card, suit):
        super().__init__(card, suit)

    def __str__(self):
        return "{} of {}".format(self.card, self.suit)

    @property
    def value(self):
        return HighCard.ranks.index(self.card)

class Deck(Cards.Deck):
    def populate(self):
        for suit in HighCard.suits:
            for card in HighCard.ranks:
                self.cards.append(HighCard(card, suit))

    def deal(self, hands, per_hand=1):
        for _ in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards.pop(0)
                    hand.receive_card(top_card)

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None

    def receive_card(self, card):
        self.card = card

    def __str__(self):
        return "{} with card {}".format(self.name, self.card)

class HighestCardGame:
    def __init__(self, names):
        self.players = [Player(name) for name in names]
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # Deal one card to each player
        self.deck.deal(self.players)
        for player in self.players:
            print("{} received {}".format(player.name, player.card))

        # Determine the winner
        highest_value = max(player.card.value for player in self.players)
        winners = [player for player in self.players if player.card.value == highest_value]

        if len(winners) > 1:
            print("\nIt's a draw between: {}!".format(', '.join([winner.name for winner in winners])))
        else:
            print("\nAnd the winner is... {}!".format(winners[0].name))

def main():
    print("**** Highest Card Game ****")
    print(""" """)
    names = []
    number = Games.askForNumber("How many players? (2-7): ", low=2, high=8)
    print()
    for i in range(number):
        name = input("Enter player name: ")
        if name == "":
            names.append("Anon")
        else:
            names.append(name)
        print()
    
    game = HighestCardGame(names)
    game.play()

if __name__ == "__main__":
    main()