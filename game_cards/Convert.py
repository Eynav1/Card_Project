# from Card import Card
#
#
# class Convert:
#     def __init__(self,card:Card):
#         """מקבל קלף עם ערך וסמל מספריים"""
#         self.card = card
#         if type(card.value) == int:
#             self.numbers_to_value(self.card)
#         if type(card.sign)== int:
#             self.numbers_to_sign(self.card)
#
#
#     def numbers_to_sign(self, card):
#         """הופך את סמל הקלף ממספר לשם הסמל לפי ההגדרה"""
#         if card.sign == 1:
#             card.sign = "DIAMOND"
#         elif card.sign == 2:
#             card.sign = "SPADE"
#         elif card.sign == 3:
#             card.sign = "HEART"
#         elif card.sign == 4:
#             card.sign = "CLUB"
#
#
#     def numbers_to_value(self,card):
#         """הופך את ערך הקלף ממספר לשם הקלף"""
#         if card.value == 11:
#             card.value = "Jack"
#         elif card.value == 12:
#             card.value = "Queen"
#         elif card.value == 13:
#             card.value = "King"
#         elif card.value == 14:
#             card.value = "Ace"
