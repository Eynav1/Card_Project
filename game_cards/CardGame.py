from Player import Player
from DexkOfCards import DeckOfCards


class CardGame:
    def __init__(self, player1_name, player2_name, num_cards:int):
        """יוצרת משחק חדש עם שני שחקנים ומכניסה אותם למשחק"""
        if type(num_cards) != int:
            raise TypeError("num_cards must be int")
        self.player1 = Player(str(player1_name), num_cards)
        self.player2 = Player(str(player2_name), num_cards)
        self.new_game(self.player1, self.player2)

    def new_game(self, player1:Player, player2:Player):
        """מתחילה את המשחק כלומר מחלקת לשחקנים קלפים (יכולה לפעןל רק כאשר אין משחק שכבר רץ)"""
        if player1.playerDeck == []:
            deck = DeckOfCards()
            deck.cards_shuffle()
            player1.set_hand(deck)
            player2.set_hand(deck)
        else:
            print("error")
            return False

    def get_winner(self):
        """בודקת למי יש יותר קלפים ומחזירה אותו כמנצח במקרה של תיקו מחזירה None"""
        if len(self.player1.playerDeck) > len(self.player2.playerDeck):
            winner = self.player1
        elif len(self.player2.playerDeck) > len(self.player1.playerDeck):
            winner = self.player2
        else:
            winner = None
        return winner

