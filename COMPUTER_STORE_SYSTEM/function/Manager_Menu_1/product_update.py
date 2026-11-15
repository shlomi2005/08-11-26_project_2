def valid(products):
    while True:
        name = input("enter a name to the product: ")
        for prodect in products:
            if prodect["name"] == name:
                return name
            else:
                print(f"{name} not in store please enter new")


def product_update_name(name, new_name, products):

    for product in products:
        if product["name"] == name:
            product["name"] = new_name
    return product


def product_update_price(name, new_price, products):
    for product in products:
        if product["name"] == name:
            product["price"] = new_price
    return product


def product_update(name, number, products):
    for product in products:
        if product["name"] == name:
            if number == 1:
                product["active"] = True
            else:
                product["active"] = False

    return product
