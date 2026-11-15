from enable_all import inventory_show_all, inventory_search, inventory_add_stock, inventory_deduct_stock, inventory_out_of_stock, inventory_low_stock


def inventory_management():
    shlomi = [1, 2, 3, 4, 5, 6, 7]
    print("Inventory Management")
    while True:
        pick = input("""
1. Show full inventory.
2. Search for a product in stock.
3. Adding units to inventory.
4. Deduct units from inventory.
5. Displaying out-of-stock products.
6. Displaying products with low stock.
7. Go back
""")
        try:
            pick = int(pick)
        except ValueError:
            print("enter a number not a string")
            continue
        if pick not in shlomi:
            print("pleasa enter a number for list ")
            continue

        if pick == 1:
            inventory_show_all()
        if pick == 2:
            print(inventory_search())
        if pick == 3:
            inventory_add_stock()
        if pick == 4:
            inventory_deduct_stock()
        if pick == 5:
            inventory_out_of_stock()
        if pick == 6:
            inventory_low_stock()
        if pick == 7:
            break
