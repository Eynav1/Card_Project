from Card import Card
from random import shuffle, randint


class DeckOfCards:
    def __init__(self):
        self.deck = []
        for val in range(1,14):
            for sign in range(1,5):
                current_card = Card(val, sign)
                self.deck.append(current_card)
        self.ace_handler()

    def ace_handler(self):
        for card in self.deck:
            if card.value == 1:
                card.value = 14

    def cards_shuffle(self):
        shuffle(self.deck)

    def del_one(self):
        del_card = self.deck.pop(randint(0,len(self.deck)-1))
        return del_card
