from main import Item
class Item2(Item):

    def __init__(self, name: str, price: float, quantity=int):
        super().__init__(name,price,quantity) #aqui pones tus items heredados
        # Assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    # Private getter
    def name(self):
        return self.__name

    @name.setter
    #Private setter
    def name(self, value):
            self.__name = value

    @property
    # Private getter
    def price(self):
        return self.__price

    @name.setter
    #Private setter
    def price(self, value):
        self.__name = value

    @property
    # Private getter
    def quantity(self):
        return self.__quantity

    @name.setter
    #Private setter
    def quantity(self, value):
        self.__name = value

