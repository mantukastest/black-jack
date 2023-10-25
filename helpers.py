from typing import List

def calculate_points(cards: List[str]) -> int:
    """
    Calculate points
    """
    card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    points = 0
    for card in cards:  # 10H
        if len(card) == 2:
            card_value = card[0]
        elif len(card) == 3:
            card_value = card[0] + card[1]  # kitaip galima parasyti card[0:2]  nes paskutinis nesiskaiciuoja!
        else:
            raise Exception("Incorrect card value. Must be of length 2 or 3")

        points += card_values[card_value]

    if points <= 21:
        return points
    # counting aces for adjustment
    count_aces = 0
    for card in cards:
        if card[0] == "A":
            count_aces += 1
    # no aces to adjust points -> return points
    if not count_aces:
        return points

    # reducing points for each ace in hand
    while count_aces:
        points -= 10
        if points <= 21:
            return points
        count_aces -= 1

    return points


def create_deck() -> List[str]:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    types = ["H", "S", "D", "C"]
    card_deck = []

    for rank in ranks:
        for type_ in types:
            card_deck.append(rank + type_)
    return card_deck


def display_results(cards: List[str], player_name: str):

    player_points = calculate_points(cards)
    print(f"{player_name} Cards: {cards}")
    print(f"{player_name} Points: {player_points}")
    print("")