class Card:
    def __init__(self, value:int, sign):
        if type(value)!= int:
            raise ValueError("value nust be int")
        self.value = value
        self.sign = sign


    def __str__(self):
        return f"{self.value},{self.sign}"

    def __gt__(self, other):
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
        if self.value == other.value and self.sign == other.sign:
            return True
        else:
            return False
