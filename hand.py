import random 

class Card:
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank 

    def value(self):
        if self.rank in ["K", "Q", "J"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

    def draw(self):
        suits = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}  # NEW: dictionary lookup
        symbol = suits[self.suit]

        if self.rank == "10":
            return [                             
                    "┌─────────┐",
                    f"│ {self.rank}      │",
                    f"│    {symbol}    │",
                    f"│      {self.rank} │",
                    "└─────────┘",
                ]
        else: 
            return [                             
                    "┌─────────┐",
                    f"│ {self.rank}       │",
                    f"│    {symbol}    │",
                    f"│       {self.rank} │",
                    "└─────────┘",
                ]

    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def __len__(self):
        return len(self.cards)

class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def hand_total(self):
        total = 0
        aces = 0

        for card in self.cards:
            total += card.value()
            if card.rank == "A":
                aces += 1

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total 

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, index):
        return self.cards[index]



