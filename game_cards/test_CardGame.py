from unittest import TestCase , mock
from CardGame import CardGame

class TestCardGame(TestCase):
    def test_init_(self):
        game = CardGame("aaa","bbb",12)
        self.assertEqual(game.player1.name , "aaa")
        self.assertEqual(game.player2.name , "bbb")

    def test_init_invalid(self):
        invalid_game = CardGame(12, 13, 12)
        self.assertEqual(invalid_game.player1.name, "12")
        self.assertEqual(invalid_game.player2.name, "13")

    def test_init_invalid2(self):
        with self.assertRaises(TypeError):
            invalid2_game = CardGame("aaa", "bbb", "abcd")

    def test_new_game(self):
        pass

    def test_get_winner(self):
        self.fail()
