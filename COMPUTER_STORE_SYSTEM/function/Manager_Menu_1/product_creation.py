def id_len_products(products):
    id_ = len(products)+1
    return id_


def creat_produc(name, price, amount, id):
    product = {"id": id, "name": name, "price": price,
               "stock": amount, "active": True}
    return product


def add_product_to_the_list(product, products):
    products.append(product)
    return products
