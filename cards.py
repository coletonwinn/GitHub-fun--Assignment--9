class Card:
    # Represents one playing card.

    RANK_VALUES = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14
    }

    def __init__(self, rank, suit):
        self.rank = str(rank)
        self.suit = suit

        if self.rank not in self.RANK_VALUES:
            raise ValueError(f"Invalid card rank: {rank}")

        # Ace is the highest card.
        self.value = self.RANK_VALUES[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"