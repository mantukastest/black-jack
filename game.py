# Hearts, Spades, Diamonds, Clubs from 2 to 10 and J Q K A
import random
from helpers import calculate_points, create_deck, display_results

if __name__ == '__main__':

    card_deck = create_deck()
    random.shuffle(card_deck)

    dealer_cards = []
    player_cards = []

    dealer_cards.append(card_deck.pop())
    display_results(dealer_cards, "Dealer")

    for _ in range(2):  # kai nereikalinga verte ja issaugome kaip "_"
        player_cards.append(card_deck.pop())
    display_results(player_cards, "Player")

    while True:
        user_input = input("Type H for HIT, type S for STAND: ")

        if user_input == "H":
            player_cards.append(card_deck.pop())
            display_results(player_cards, "Player")
            if calculate_points(player_cards) > 21:
                print("Dealer WON!")
                quit()

        elif user_input == "S":
            break
        else:
            print("WRONG VALUE!")
            continue

    while calculate_points(dealer_cards) <= 16:
        dealer_cards.append(card_deck.pop())
        display_results(dealer_cards, "Dealer")

    if calculate_points(dealer_cards) > 21:
        print("You WON!")
    elif calculate_points(player_cards) > calculate_points(dealer_cards):
        print("You WON!")
    elif calculate_points(player_cards) < calculate_points(dealer_cards):
        print("Dealer WON!")
    else:
        print("Draw")


