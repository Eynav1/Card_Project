from DexkOfCards import DeckOfCards
from random import randint
from Card import Card


class Player:
    def __init__(self, name: str, num_of_card: int):
        self.name = name
        self.num_of_cards = num_of_card
        self.playerDeck = []
        if self.num_of_cards > 26 or self.num_of_cards < 10:
            self.num_of_cards = 26

    def __str__(self):
        return f"player: {self.name}, have{len(self.playerDeck)} cards"

    def set_hand(self, deck: DeckOfCards):
        for i in range(self.num_of_cards):
            self.playerDeck.append(deck.del_one())

    def get_card(self):
        card = self.playerDeck.pop(randint(0, len(self.playerDeck) - 1))
        return card

    def add_card(self, card: Card):
        self.playerDeck.append(card)

