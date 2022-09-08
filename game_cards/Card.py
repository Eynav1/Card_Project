class Card:
    def __init__(self, value:int, sign:int):
        """מקבל 2 משתנים מספריים שנותנים ערך וסמל לקלף ובודק שהערך בין 1-13 והסמל בין 1-4"""
        if type(value) != int:
            raise TypeError("value nust be int")
        if value < 1 or value > 13:
            raise ValueError("value nust be 1 - 13")
        if type(sign) != int:
            raise TypeError("value nust be int")
        if sign > 4 or sign < 1:
            raise ValueError("sign nust be 1 - 4")
        self.value = value
        self.sign = sign

    def change_for_print(self):
        if self.sign == 1:
            self.sign = "DIAMOND"
        elif self.sign == 2:
            self.sign = "SPADE"
        elif self.sign == 3:
            self.sign = "HEART"
        elif self.sign == 4:
            self.sign = "CLUB"
        if self.value == 11:
            self.value = "Jack"
        elif self.value == 12:
            self.value = "Queen"
        elif self.value == 13:
            self.value = "King"
        elif self.value == 14:
            self.value = "Ace"
    def __str__(self):
        self.change_for_print()
        return f"{self.value},{self.sign}"

    def __repr__(self):
        self.change_for_print()
        return f"{self.value},{self.sign}"

    def __gt__(self, other):
        """עוזר בהשוואה בין קלף נוכחי לקלף שהוא מקבל"""
        if self.sign == "DIAMOND":
            self.sign = 1
        elif self.sign == "SPADE":
            self.sign = 2
        elif self.sign == "HEART":
            self.sign = 3
        elif self.sign == "CLUB":
            self.sign = 4
        if other.sign == "DIAMOND":
            other.sign = 1
        elif other.sign == "SPADE":
            other.sign = 2
        elif other.sign == "HEART":
            other.sign = 3
        elif other.sign == "CLUB":
            other.sign = 4
        if self.value == "Jack":
            self.value = 11
        elif self.value == "Queen":
            self.value = 12
        elif self.value == "King":
            self.value = 13
        elif self.value == "Ace":
            self.value = 14
        if other.value == "Jack":
            other.value = 11
        elif other.value == "Queen":
            other.value = 12
        elif other.value == "King":
            other.value = 13
        elif other.value == "Ace":
            other.value = 14
        if self.value > other.value:
            return True
        elif self.value < other.value:
            return False
        elif self.value == other.value:
            if self.sign > other.sign:
                return True
            elif self.sign < other.sign:
                return False

    def __eq__(self, other):
        """מחזיר משתנה בוליאני אם גם הסמל וגם הערך שווים"""
        if self.value == other.value and self.sign == other.sign:
            return True
        else:
            return False
