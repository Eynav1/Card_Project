from CardGame import CardGame
# from Convert import Convert
from Player import Player

name1 = "Eynav"
name2 = "Amit"
num_of = 26


# def convert_before_print():
#     """הופך את הקלפים שנזרקו מערכים מספריים לשמותיהם"""
#     Convert(p1_card)
#     Convert(p2_card)


def print_thrown_cards():
    """מדפיס את הקלפים ושמות השחקנים"""
    print(our_game.player2.name, p2_card)
    print(our_game.player1.name, p1_card)


def collect_to_winner(first_player: Player, second_player: Player):
    """אוסף את הקלפים למנצח"""
    first_player.add_card(p1_card)
    second_player.add_card(p2_card)


our_game = CardGame(name1, name2, num_of)
print(name1, our_game.player1.playerDeck)
print(name2, our_game.player2.playerDeck)
count_p1_winning = 0
count_p2_winning = 0
for i in range(10):
    p1_card = our_game.player1.get_card()
    p2_card = our_game.player2.get_card()
    if p1_card > p2_card:
        count_p1_winning += 1
        # convert_before_print()
        print_thrown_cards()
        collect_to_winner(our_game.player1, our_game.player1)

        print("this round winner: ", our_game.player1)
    elif p2_card > p1_card:
        count_p2_winning += 1
        # convert_before_print()
        print_thrown_cards()
        collect_to_winner(our_game.player2, our_game.player2)

        print("this round winner: ", our_game.player2)
    else:
        # convert_before_print()
        print_thrown_cards()
        collect_to_winner(our_game.player1, our_game.player2)

        print("no one win this round")

if count_p2_winning > count_p1_winning:
    print(our_game.player2)
elif count_p1_winning > count_p2_winning:
    print(our_game.player1)
else:
    print("no one win this game")
