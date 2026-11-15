def search_by_name(name, products):
    search_product = []

    for product in products:
        if name.lower() in product["name"].lower():
            search_product.append(product)

    if not search_product:
        print(f"{name} not in store please enter a product other")

    return search_product
