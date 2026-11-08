class Product:
    def __init__(self, name, price, quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new):
        if new > 0:
            self.__price = new
        else:
            raise ValueError("price must be positive")

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    def add_stock(self, new_quantity):
        if new_quantity <= 0:
            raise ValueError("amount must be positive")
        self.__quantity += new_quantity

    def sell(self, emaut):
        if emaut > self.__quantity:
            raise ValueError(f"not enough {self.__name}")
        self.__quantity -= emaut

    @property
    def total_value(self):
        return self.__price * self.__quantity

    def __str__(self):
        return f"{self.__name},{self.__price},{self.__quantity}"
