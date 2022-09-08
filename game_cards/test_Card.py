from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        # valid ace diamond (1, 1)
        self.ace_D = Card(1,1)
        self.king_C = Card(13,4)

    # valid ace test (1,1)
    # valid  king test (1,1)
    #  ולידי איניט מקבלת ערכי קצה
    def test_init_valid(self):
        self.assertEqual(self.ace_D.value, 1)
        self.assertEqual(self.ace_D.sign, 1)
        self.assertEqual(self.king_C.value, 13)
        self.assertEqual(self.king_C.sign, 4)

    # invalid card value is 0
    # איניט מקבלת ערכי קצה לא ולידי
    def test_init_invalid_value1(self):
        with self.assertRaises(ValueError):
            invalid_card = Card(0, 1)
            invalid_card = Card(-1, 1)
            invalid_card = Card(14, 1)
    # איניט מקבלת ערך str לערך הקלף לא ולידי
    def test_init_invalid_value2(self):
        with self.assertRaises(TypeError):
            invalid_card = Card("abc", 1)
    # איניט מקבלת ערכי קצה לא ולידי לסימן הקלף
    def test_init_invalid_sign1(self):
        with self.assertRaises(ValueError):
            self.invalid_card = Card(4, 0)
            self.invalid_card = Card(4, -1)
            self.invalid_card = Card(4, 5)
    # איניט מקבלת ערך str לסימן הקלף לא ולידי
    def test_init_invalid_sign2(self):
        with self.assertRaises(TypeError):
            invalid_card = Card(2, "abc")

    # בדיקת השוואה ולידית
    def test_eq_valid(self):
        self.assertTrue(self.ace_D == self.ace_D)
        self.assertFalse(self.ace_D == self.king_C)

    # בדיקת השוואה לערכים וסימנים לא ולידים
    def test_eq_invalid(self):
        self.ace_D.value = 15
        self.king_C.value = 15
        self.assertFalse(self.king_C == self.ace_D)
        self.king_C.sign = 1
        self.assertTrue(self.king_C == self.ace_D)
        self.king_C.sign = 5
        self.ace_D.sign = 5
        self.assertTrue(self.king_C == self.ace_D)

    # בדיקה מי יותר גדול ולידי
    def test_gt_valid(self):
        card1 = Card(7, 1)
        card2 = Card(8, 3)
        card3 = Card(9, 2)
        card4 = Card(9, 4)

        # value and sign
        self.assertTrue(card1 < card2)
        # only value
        self.assertTrue(card3 > card2)
        # only sign
        self.assertTrue(card3 < card4)
