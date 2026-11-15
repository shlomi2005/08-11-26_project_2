def get_positive_number(message):
    number = input(message).strip()
    while not number.isdigit() or int(number) == 0:
        print("please enter a whole number bigger than 0")
        number = input(message).strip()
    return int(number)


def show_all(products):
    for product in products:
        if product["active"]:
            print(f"name = {product['name']} stock {product['stock']}")


def search_inventory(name, products):
    for product in products:
        if name == product["name"]:
            return f"{name} = stock {product['stock']}"
    return "product not found"


def name_for_product():
    name_ = input("enter a name to the product: ").strip()
    return name_


def add_stock(name, products):
    for product in products:
        if name == product["name"]:
            new_stock = get_positive_number(
                "How many products do you want to add to the inventory? ")
            product["stock"] += new_stock
            print("The quantity has been successfully changed")
            break
    else:
        print("product not found")


def deduct_units_from_inventory(name, products):
    for product in products:
        if name == product["name"]:
            new_stock = get_positive_number(
                "How many products would you like to destock? ")
            if new_stock > product["stock"]:
                print(
                    f"not enough in stock, there are only {product['stock']}")
            else:
                product["stock"] -= new_stock
                print("The quantity has been successfully changed")
            break
    else:
        print("product not found")


def products_with_0_stock(products):
    found = False
    for product in products:
        if product["active"] and product["stock"] == 0:
            print(product)
            found = True
    if not found:
        print("no products out of stock")


def products_with_low_stock(products, threshold=5):
    found = False
    for product in products:
        if product["active"] and product["stock"] < threshold:
            print(product)
            found = True
    if not found:
        print("No products with low stock")
