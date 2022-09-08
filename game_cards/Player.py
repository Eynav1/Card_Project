from DexkOfCards import DeckOfCards
from random import randint
from Card import Card


class Player:
    def __init__(self, name: str, num_of_card: int):
        """מקבל שם ומספר קלפים לחלוקה לא יעלה על 26 ולא ירד מ10"""
        self.name = name
        self.num_of_cards = num_of_card
        self.playerDeck = []
        if self.num_of_cards > 26 or self.num_of_cards < 10:
            self.num_of_cards = 26

    def __str__(self):
        return f"player: {self.name}, have: {len(self.playerDeck)} cards"

    def set_hand(self, deck: DeckOfCards):
        """מחלק קלפים לשחקן מהחבילה המלאה"""
        for i in range(self.num_of_cards):
            self.playerDeck.append(deck.del_one())

    def get_card(self):
        """מוציא קלף מהחבילה של השחקן ומחזיר אותו"""
        card = self.playerDeck.pop(randint(0, len(self.playerDeck) - 1))
        return card

    def add_card(self, card: Card):
        """מוסיף קלף לחבילת השחקן"""
        self.playerDeck.append(card)

