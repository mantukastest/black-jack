 # Hearts, Spades, Diamonds, Clubs from 2 to 10 and J Q K A

import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
types = ["H", "S", "D", "C"]
card_deck = []

for rank in ranks:
    for type_ in types:
        card_deck.append(rank+type_)

random.shuffle(card_deck)   #ismaiso kortu kalade

# print(card_deck)

# random_card = random.choice(card_deck)      #isrenka random korta is kalades, bet ji ir lieka kaladeje

# random_card = card_deck.pop()               #istraukia random korta is kalades ir jos kaladeje nebelieka


#susikurti useri ir krupje
# player listas ir dealer listas
# zaidejas gauna 2 kortas, krupje 1
#pasiskaityt apie komanda prompt (duoda galimybe useriui programos metu ivedineti teksa)

dealer = []
player = []

dealer.append(card_deck.pop())
print(f" Dealer Cards: {dealer}")

player.append(card_deck.pop())
player.append(card_deck.pop())
print(f" Your Cards: {player}")

print("")

user_input = input("Type H for HIT, type S for STAND: ")

if user_input == "H":
    player.append(card_deck.pop())
    print(f" Your Cards: {player}")
    print(f" Dealer Cards: {dealer}")
elif user_input == "S":
    dealer.append(card_deck.pop())
    print(f" Your Cards: {player}")
    print(f" Dealer Cards: {dealer}")
else:
    user_input = input("Wrong value! Type H for HIT, type S for STAND: ")

# Pasirasyt funkcija, kai printini dealer cards ir player cards kad grazintu kiek tasku turi
# kita funkcija turi patikrinti ar player dar nepralose (taip kaip siandien mokemes)
# turi atsirasti loopas, kuris suktusi iki zaidimo pabaigos, useris gali rinktis kortas kol pas ji nedaugiau nei 21
# kai useris sustoja dealeris turi rinkti toliau kortas