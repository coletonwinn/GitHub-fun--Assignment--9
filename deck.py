import random
from cards import Card


class Deck:

    def __init__(self):
        # Creates an empty list for the cards.
        self.cards = []

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        ranks = [
            "2", "3", "4", "5", "6", "7", "8",
            "9", "10", "Jack", "Queen", "King", "Ace"
        ]

        # Creates all 52 cards.
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        # Randomly shuffles the deck.
        random.shuffle(self.cards)

    def draw_card(self):
        # Removes and returns one card.
        if len(self.cards) > 0:
            return self.cards.pop()

        return None

    def add_cards(self, cards):
        # Adds collected cards to the deck.
        self.cards.extend(cards)

    def cards_remaining(self):
        # Returns the number of cards left.
        return len(self.cards)