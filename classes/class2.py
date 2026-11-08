from classes.oop import Product


class Inventory:
    __products = []

    def add(self, product):
        if self.find(product.name) is not None:
            raise ValueError(f"{product.name} already exists")
        self.__products.append(product)

    def find(self, name):
        for product in self.__products:
            if product.name == name:
                return product
        return None

    def by_value(self):
        sorted_list = sorted(self.__products,
                             key=lambda k: k.total_value, reverse=True)
        return sorted_list

    @property
    def total_value(self):
        return sum(product.total_value for product in self.__products)
