from CardGame import CardGame
from Convert import Convert

name1 = "Eynav"
name2 = "Amit"
num_of = 26

our_game = CardGame(name1,name2,num_of)
count_p1_winning = 0
count_p2_winning = 0
for i in range(10):
    p1_card = our_game.player1.get_card()
    p2_card = our_game.player2.get_card()
    if p1_card > p2_card:
        our_game.player1.add_card(p1_card)
        our_game.player1.add_card(p2_card)
        count_p1_winning += 1
        sign1 = Convert(p1_card)
        sign2 = Convert(p2_card)

        print(our_game.player2.name, p2_card)
        print(our_game.player1.name, p1_card)
        print("this round winner:",our_game.player1)
    elif p2_card > p1_card:
        our_game.player2.add_card(p1_card)
        our_game.player2.add_card(p2_card)
        count_p2_winning += 1
        sign1 = Convert(p1_card)
        sign2 = Convert(p2_card)

        print(our_game.player2.name, p2_card)
        print(our_game.player1.name, p1_card)
        print("this round winner:",our_game.player2)
    else:
        our_game.player1.add_card(p1_card)
        our_game.player2.add_card(p2_card)
        sign1 = Convert(p1_card)
        sign2 = Convert(p2_card)

        print(our_game.player2.name, p2_card)
        print(our_game.player1.name, p1_card)
        print("no one win this round")

if count_p2_winning > count_p1_winning:
    print(our_game.player2)
elif count_p1_winning > count_p2_winning:
    print(our_game.player1)
else:
    print("no one win this game")
