from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        # valid ace diamond (1, 1)
        self.ace_D = Card(1,1)

    # valid lower test (1,1)
    def test_init_valid(self):
        self.assertEqual(self.ace_D.value, 1)
        self.assertEqual(self.ace_D.sign, 1)

    # invalid card value is 0
    def test_init_invalid_1(self):
        with self.assertRaises(ValueError):
            self.invalid_card = Card(0, 1)
            self.invalid_card = Card(-1, 1)
            self.invalid_card = Card(14, 1)





