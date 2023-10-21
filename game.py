 # Hearts, Spades, Diamonds, Clubs from 2 to 10 and J Q K A

import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
types = ["H", "S", "D", "C"]
card_deck = []

for rank in ranks:
    for type_ in types:
        card_deck.append(rank+type_)

random.shuffle(card_deck)   #ismaiso kortu kalade

dealer_cards = []
player_cards = []

dealer_cards.append(card_deck.pop())
print(f" Dealer Cards: {dealer_cards}")

player_cards.append(card_deck.pop())
player_cards.append(card_deck.pop())
print(f" Your Cards: {player_cards}")

print("")

user_input = input("Type H for HIT, type S for STAND: ")

if user_input == "H":
    player_cards.append(card_deck.pop())
    dealer_cards.append(card_deck.pop())
    print(f" Dealer Cards: {dealer_cards}")
    print(f" Your Cards: {player_cards}")
elif user_input == "S":
    dealer_cards.append(card_deck.pop())
    print(f" Dealer Cards: {dealer_cards}")
    print(f" Your Cards: {player_cards}")
else:
    user_input = input("WRONG VALUE! Type H for HIT, type S for STAND: ")

# Pasirasyt funkcija, kai printini dealer cards ir player cards kad grazintu kiek tasku turi
# kita funkcija turi patikrinti ar player dar nepralose (taip kaip siandien mokemes)
# turi atsirasti loopas, kuris suktusi iki zaidimo pabaigos, useris gali rinktis kortas kol pas ji nedaugiau nei 21
# kai useris sustoja dealeris turi rinkti toliau kortas


card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6":6, "7": 7, "8":8, "9": 9, "J": 10, "Q": 10, "K": 10, "A": 11}

def calculate_points(cards):
    points = 0
    for card in cards:
        rank = card[:-1]  # Extract the rank of the card (e.g., '2' from '2H')
        points += card_values.get(rank, 0)  # Use get() to handle cases like 'A' where the value can be 11 or 1
    return points

dealer_points = calculate_points(dealer_cards)
player_points = calculate_points(player_cards)


print(f"Dealer Points: {dealer_points}")
print(f"Player Points: {player_points}")

if player_points > 21:
    print("GAME OVER")
elif player_points < dealer_points:
    print("GAME OVER")
else:
    print("YOU WON!")


# Blogai skaiciuoja su skaicium 10!
# Po zinutes Wrong Value neberodo kortu, tik value ir ar laimejai