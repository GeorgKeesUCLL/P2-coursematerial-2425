class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched Currencies!")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched Currencies!")
        
    def __mul__(self, other):
        return Money(self.amount*other, self.currency)

    @property
    def amount(self):
        return self.__amount
    
    @property
    def currency(self):
        return self.__currency