import random

card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
               "A": 11}
types = ["H", "S", "D", "C"]


class Card:
    def __init__(self, rank: str, type_: str):  # konstruktorius, kuris kvieciamas klaseje tik karta!
        if rank not in card_values.keys():
            raise ValueError(f'Not allowed card rank: {rank}')
        if type_.upper() not in types:
            raise ValueError(f'Not allowed card type: {type_}')
        self.rank = rank
        self.type_ = type_.upper()

    def __str__(self) -> str:
        return f"Card {self.rank} of {self.type_}. Points: {self.get_points()}"

    def get_points(self) -> int:
        points = card_values.get(self.rank)
        return points


class Deck:
    def __init__(self):
        self.cards = []
        for rank in card_values.keys():
            for type_ in types:
                card = Card(rank, type_)
                self.cards.append(card)
                # susikurt kortu kalade, kortu kalade turi tureti dar pora metodu, isdalinti ir sumaisyti ir paziuret i 14 eilute. susikurti zaidejo objekta. privesti veikti su objektais programa

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        return self.cards.pop()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"Player {self.name} has {[str(c) for c in self.hand]} cards. score: {self.points()}"

    def take_card(self, card: Card):
        self.hand.append(card)

    def points(self) -> int:
        points = 0
        for card in self.hand:  # 10H
            points += card.get_points()

        if points <= 21:
            return points
        # counting aces for adjustment
        count_aces = 0
        for card in self.hand:
            if card.rank == "A":
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


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    nick = Player(name="Nick")
    dealer = Player(name="Dealer")

    card = deck.deal_card()
    dealer.take_card(card)

    for _ in range(2):
        card = deck.deal_card()
        nick.take_card(card)

    print(dealer)
    print(nick)

    while True:
        user_input = input("Type H for HIT, type S for STAND: ")

        if user_input == "H":
            card = deck.deal_card()
            nick.take_card(card)
            print(nick)

            if nick.points() > 21:
                print("Dealer WON!")
                quit()

        elif user_input == "S":
            break
        else:
            print("WRONG VALUE!")
            continue

    while dealer.points() <= 16:
        dealer.take_card(deck.deal_card())
        print(dealer)

    if dealer.points() > 21:
        print("You WON!")
    elif nick.points() > dealer.points():
        print("You WON!")
    elif nick.points() < dealer.points():
        print("Dealer WON!")
    else:
        print("Draw")
