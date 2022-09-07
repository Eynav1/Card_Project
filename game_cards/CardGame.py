from Player import Player
from DexkOfCards import DeckOfCards


class CardGame:
    def __init__(self, player1_name, player2_name, num_cards:int):
        self.player1 = Player(player1_name, num_cards)
        self.player2 = Player(player2_name, num_cards)
        self.new_game(self.player1, self.player2)

    def new_game(self, player1:Player, player2:Player):
        if player1.playerDeck == []:
            deck = DeckOfCards()
            deck.cards_shuffle()
            player1.set_hand(deck)
            player2.set_hand(deck)
        else:
            print("error")

    def get_winner(self):
        if self.player1.playerDeck > self.player2.playerDeck:
            winner = self.player1
        elif self.player2.playerDeck > self.player1.playerDeck:
            winner = self.player2
        else:
            winner = None
        return winner

