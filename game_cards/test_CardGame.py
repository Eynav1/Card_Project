from unittest import TestCase , mock
from CardGame import CardGame

class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("aaa","bbb",12)
    def test_init_(self):
        self.game = CardGame("aaa","bbb",12)
        self.assertEqual(self.game.player1.name , "aaa")
        self.assertEqual(self.game.player2.name , "bbb")

    def test_init_invalid(self):
        invalid_game = CardGame(12, 13, 12)
        self.assertEqual(invalid_game.player1.name, "12")
        self.assertEqual(invalid_game.player2.name, "13")

    def test_init_invalid2(self):
        with self.assertRaises(TypeError):
            invalid2_game = CardGame("aaa", "bbb", "abcd")


    def test_new_game1(self):
        self.assertFalse(self.game.new_game(self.game.player1,self.game.player2))


    def test_get_winner(self):
        self.assertTrue(self.game.get_winner(),None)


    def test_get_winner2(self):
        self.game.player1.playerDeck = [(2,2)]
        self.assertTrue(self.game.get_winner(),self.game.player2)

    def test_get_winner3(self):
        self.game.player2.playerDeck = [(2,2)]
        self.assertTrue(self.game.get_winner(),self.game.player1)

