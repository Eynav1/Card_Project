from Card import Card
from random import shuffle, randint


class DeckOfCards:
    def __init__(self):
        """מייצר חבילת קלפים מסוג ליסט"""
        self.deck = []
        for val in range(1,14):
            for sign in range(1,5):
                current_card = Card(val, sign)
                self.deck.append(current_card)
        self.ace_handler()

    def ace_handler(self):
        """במידה וערך הקלף הוא 1 (אס) הוא ממיר את הערך ל14 כדי שהאס יהיה הקלף הכי חזק"""
        for card in self.deck:
            if card.value == 1:
                card.value = 14

    def cards_shuffle(self):
        """מערבב את החבילה"""
        shuffle(self.deck)

    def del_one(self):
        """שולף בצורה רנדומלית קלף מהחבילה (מוציא אותו) ומחזיר את הקלף ששלף"""
        del_card = self.deck.pop(randint(0,len(self.deck)-1))
        return del_card
