# # kortu kalade yra listas.
# # korta tai yra stringas susidedantis is 2 simboliu (skaicius ir rusis)
# # hearts, spades, diamonds, clubs from 2 to 10 and j q k a
#
# # struktura kaip atskirti kortas
# # sugalvoti kaip paemus viena korta is kalades, kad kaladeje tos kortos neliktu
#
#

hearts = ["h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk", "ha"]

spades = ["s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "sa"]

diamonds = ["d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk", "da"]

clubs = ["c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck", "ca"]

cards = [hearts, spades, diamonds, clubs]

print(len(cards))

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
types = ["H", "S", "D", "C"]
card_deck = []

for rank in ranks:
    for type_ in types:
        card_deck.append(rank+type_)

print(card_deck)

#ismaisytu kortu kalade
#issitraukti random korta