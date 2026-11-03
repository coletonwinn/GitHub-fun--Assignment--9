
from deck import Deck
from player import Player


def play_game():

    print("Welcome to Two-Deck War!")

    # Create two separate decks.
    deck1 = Deck()
    deck2 = Deck()

    # Shuffle both decks.
    deck1.shuffle()
    deck2.shuffle()

    # Create two players.
    player1 = Player("Player 1", deck1)
    player2 = Player("Player 2", deck2)

    round_number = 1

    # Continue until one player has all 104 cards.
    while player1.card_count() < 104 and player2.card_count() < 104:

        print(f"\n--- Round {round_number} ---")

        # Store all cards played during the round.
        cards_in_play = []

        # Both players draw a card.
        card1 = player1.draw_card()
        card2 = player2.draw_card()

        cards_in_play.extend([card1, card2])

        print(f"{player1.name} drew the {card1}.")
        print(f"{player2.name} drew the {card2}.")

        # Compare cards until someone wins.
        while True:

            if card1.value > card2.value:

                if len(cards_in_play) > 2:
                    print(f"{player1.name} wins the war!")
                else:
                    print(f"{player1.name} wins the round!")

                player1.collect_cards(cards_in_play)
                break

            elif card2.value > card1.value:

                if len(cards_in_play) > 2:
                    print(f"{player2.name} wins the war!")
                else:
                    print(f"{player2.name} wins the round!")

                player2.collect_cards(cards_in_play)
                break

            else:
                print("War!")

                # Check whether both players can continue.
                if player1.card_count() == 0:
                    print(f"{player2.name} wins because "
                          f"{player1.name} ran out of cards!")
                    player2.collect_cards(cards_in_play)
                    break

                if player2.card_count() == 0:
                    print(f"{player1.name} wins because "
                          f"{player2.name} ran out of cards!")
                    player1.collect_cards(cards_in_play)
                    break

                # Both players draw another card.
                card1 = player1.draw_card()
                card2 = player2.draw_card()

                cards_in_play.extend([card1, card2])

                print(f"{player1.name} drew the {card1}.")
                print(f"{player2.name} drew the {card2}.")

        # Display how many cards each player has.
        print(f"{player1.name} has {player1.card_count()} cards.")
        print(f"{player2.name} has {player2.card_count()} cards.")

        # Check that all 104 cards are accounted for.
        print("Total cards:",
              player1.card_count() + player2.card_count())

        round_number += 1

        # Check if someone has won.
        if player1.card_count() == 104:
            break

        if player2.card_count() == 104:
            break

        input("Press Enter to play the next round.")

    # Announce the final winner.
    print(f"\nGame finished after {round_number - 1} rounds.")

    if player1.card_count() == 104:
        print(f"{player1.name} has collected all the cards!")
        print(f"{player1.name} wins the game!")

    else:
        print(f"{player2.name} has collected all the cards!")
        print(f"{player2.name} wins the game!")


# Start the game.
if __name__ == "__main__":
    play_game()