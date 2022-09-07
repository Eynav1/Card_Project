from unittest import TestCase
from Player import Player
from DexkOfCards import DeckOfCards
from Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.player_valid1 = Player("aaa", 26)
        self.player_valid2 = Player("bbb", 10)
        self.big_deck = DeckOfCards()
        self.ace_D = Card(1,1)

    def test_init_valid(self):
        # player_valid1 = Player("aaa",26)
        # player_valid2 = Player("bbb",10)
        self.assertTrue(self.player_valid1.name == "aaa")
        self.assertTrue(self.player_valid1.num_of_cards == 26)
        self.assertTrue(self.player_valid2.name == "bbb")
        self.assertTrue(self.player_valid2.num_of_cards == 10)

    def test_init_invalid(self):
        player_invalid1 = Player(12, 26)
        player_invalid2 = Player("bbb", 9)
        player_invalid3 = Player("bbb", 27)
        player_invalid4 = Player("bbb", -1)
        self.assertTrue(player_invalid1.name, "12")
        self.assertTrue(player_invalid2.num_of_cards, 26)
        self.assertTrue(player_invalid3.num_of_cards, 26)
        self.assertTrue(player_invalid4.num_of_cards, 26)


    def test_set_hand(self):
        self.player_valid1.set_hand(self.big_deck)
        self.assertTrue(len(self.big_deck.deck),26)
        self.assertTrue(len(self.player_valid1.playerDeck),26)
        for i in self.player_valid1.playerDeck:
            self.assertNotIn(i, self.big_deck.deck)


    def test_get_card(self):
        self.player_valid1.set_hand(self.big_deck)
        start = len(self.player_valid1.playerDeck)
        current_card = self.player_valid1.get_card()
        after_get = len(self.player_valid1.playerDeck)
        self.assertEqual(start - 1, after_get)
        self.assertNotIn(current_card, self.player_valid1.playerDeck)




    def test_add_card(self):
        self.player_valid1.set_hand(self.big_deck)
        self.player_valid1.add_card(self.ace_D)
        self.assertIn(self.ace_D,self.player_valid1.playerDeck)
