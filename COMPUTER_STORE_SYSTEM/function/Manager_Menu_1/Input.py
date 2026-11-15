def string():
    name_product = input("enter a name of the product: ").strip()

    return name_product


def new_name_up():
    new_name = input("enter a new number: ").strip()
    return new_name


def new_price_up():
    while True:
        try:
            new_price = int(input("enter a new price: "))
        except ValueError:
            print("the number must consist of whole numbers only.")
            continue
        if new_price > 0:
            return new_price
        else:
            print("Please enter a positive number.")


def get_number():
    while True:
        try:
            num = int(input("enter a price for product: "))
        except ValueError:
            print("the number must consist of whole numbers only.")
            continue
        if num > 0:
            return num
        else:
            print("Please enter a positive number.")


def get_inventory():
    while True:
        try:
            inventory = int(input("enter a inventory for product: "))
        except ValueError:
            print("the number must consist of whole numbers only.")
            continue
        if inventory > 0:
            return inventory
        else:
            print("Please enter a positive number.")


def new_active_up():
    shlomi = [1, 2]
    while True:
        try:
            new_active = int(
                input("To order, press 1; if unavailable, press 2: "))

        except ValueError:
            print("the number must consist of whole numbers only.")
            continue
        if new_active in shlomi:
            return new_active
        else:
            print("Please enter a number (1-2).")
