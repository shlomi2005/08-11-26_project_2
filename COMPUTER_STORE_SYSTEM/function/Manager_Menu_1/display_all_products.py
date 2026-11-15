def despley(products):
    available_products = []
    for product in products:
        if product["active"] == True:
            available_products.append(product)
    return available_products
