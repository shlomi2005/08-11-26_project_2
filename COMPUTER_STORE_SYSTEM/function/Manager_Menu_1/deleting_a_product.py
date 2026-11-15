def deleting_valid(products):
    while True:
        number_id = int(input("enter a id to the product: "))

        for product in products:
            if product["id"] == number_id:
                return number_id

        print("id not in products please enter new id ")


def delit(number_id, products):
    y_n = input("Are you sure you want to delete?  y or n ")
    if y_n == "y":
        for product in products:
            if product["id"] == number_id:
                products.remove(product)
                print("the product successfully deleted")
                break
    else:
        print("The product was not deleted.")
    return products
