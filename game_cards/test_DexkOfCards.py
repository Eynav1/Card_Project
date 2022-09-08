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
        ace_deck = DeckOfCards()
        ace_card = Card(1,1)
        other_ace = Card(1,1)
        other_ace.value = 14
        ace_deck.deck = [ace_card]
        self.assertFalse(ace_deck.deck == [other_ace])
        ace_deck.ace_handler()
        self.assertTrue(ace_deck.deck == [other_ace])

    def test_ace_handler_invalid(self):
        not_ace_deck = DeckOfCards()
        not_ace_card = Card(2, 1)
        other_ace = Card(1, 1)
        other_ace.value = 14
        not_ace_deck.deck = [not_ace_card]
        self.assertFalse(not_ace_deck.deck == [other_ace])
        not_ace_deck.ace_handler()
        self.assertFalse(not_ace_deck.deck == [other_ace])

    def test_cards_shuffle(self):
        self.assertTrue(self.deck != self.deck.cards_shuffle())

    def test_del_one(self):
        start = len(self.deck.deck)
        self.deck.del_one()
        after_del = len(self.deck.deck)
        self.assertTrue(start-1 == after_del)


