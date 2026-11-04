class Player:

    def __init__(self, name, deck):
        # Stores the player's name and deck.
        self.name = name
        self.deck = deck

    def draw_card(self):
        # Draws a card from the player's deck.
        return self.deck.draw_card()

    def collect_cards(self, cards):
        # Adds won cards to the player's deck.
        self.deck.add_cards(cards)

    def card_count(self):
        # Returns the number of cards the player has.
        return self.deck.cards_remaining()