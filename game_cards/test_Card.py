from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        # valid ace diamond (1, 1)
        self.ace_D = Card(1,1)
        self.king_C = Card(13,4)

    # valid lower test (1,1)
    def test_init_valid(self):
        self.assertEqual(self.ace_D.value, 1)
        self.assertEqual(self.ace_D.sign, 1)
        self.assertEqual(self.king_C.value, 13)
        self.assertEqual(self.king_C.sign, 4)

    # invalid card value is 0
    def test_init_invalid_value1(self):
        with self.assertRaises(ValueError):
            invalid_card = Card(0, 1)
            invalid_card = Card(-1, 1)
            invalid_card = Card(14, 1)

    def test_init_invalid_value2(self):
        with self.assertRaises(TypeError):
            invalid_card = Card("abc", 1)

    def test_init_invalid_sign1(self):
        with self.assertRaises(ValueError):
            self.invalid_card = Card(4, 0)
            self.invalid_card = Card(4, -1)
            self.invalid_card = Card(4, 5)

    def test_init_invalid_sign2(self):
        with self.assertRaises(TypeError):
            invalid_card = Card(2, "abc")

    def test_eq_(self):
        card1 = Card(7,1)
        self.assertTrue(card1 == card1)

    def test_gt_(self):
        card1 = Card(7, 1)
        card2 = Card(8, 2)
        card3 = Card(9, 3)
        card4 = Card(9, 4)

        self.assertTrue(card1 < card2)
        self.assertTrue(card3 > card2)
        self.assertFalse(card3 > card4)
        self.assertTrue(card3 < card4)







