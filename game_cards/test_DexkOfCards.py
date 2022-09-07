from unittest import TestCase
from DexkOfCards import DeckOfCards
from Card import Card

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_(self):
        self.assertTrue(len(self.deck.deck), 52)
        for i in self.deck.deck:
            self.assertEqual(self.deck.deck.count(i), 1)

    def test_ace_handler(self):
        ace_card = Card(1,1)
        self.assertTrue(ace_card.value , 14)

    def test_cards_shuffle(self):
        self.assertTrue(self.deck != self.deck.cards_shuffle())

    def test_del_one(self):
        start = len(self.deck.deck)
        self.deck.del_one()
        after_del = len(self.deck.deck)
        self.assertTrue(start-1 == after_del)


