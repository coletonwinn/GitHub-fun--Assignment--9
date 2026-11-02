import random
from cards import Card


class Deck:
   def __init__(self):
       #creates an empty list for the cards
       self.cards = []


       suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
       ranks = range(2, 15)


       for suit in suits:
           for rank in ranks:
               card = Card(rank, suit)
               self.cards.append(card)


   def shuffle(self):
       random.shuffle(self.cards)


   def draw_card(self):
       if len(self.cards) > 0:
           return self.cards.pop(0)
       return None


   def add_cards(self, cards):
       self.cards.extend(cards)


   def cards_remaining(self):
       return len(self.cards)





