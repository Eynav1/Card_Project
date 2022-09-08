from unittest import TestCase
from Convert import Convert
from Card import Card


class TestConvert(TestCase):
    def setUp(self):
        self.ace_D = Card(1,1)
        self.king_s = Card(13,2)
        self.Queen_H = Card(12,3)
        self.jack_c = Card(11,4)
    def test_init_(self):
        self.assertTrue("Ace", "DIAMOND" == Convert(self.ace_D))
        self.assertTrue("King", "SPADE" == Convert(self.king_s))
        self.assertTrue("Queen", "HEART" == Convert(self.Queen_H))
        self.assertTrue("Jack", "CLUB" == Convert(self.jack_c))

    def test_numbers_to_sign(self):
        pass

    def test_numbers_to_value(self):
        pass
