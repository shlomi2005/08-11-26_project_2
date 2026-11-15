from enable_all import enable, Product_display_true, search_by_name_1, update_meneger, manager_delet
from function.Manager_Menu_1.display_all_products import despley


def products_management():
    shlomi = [1, 2, 3, 4, 5, 6]
    print("--------- PRODUCTS MANAGEMENT ---------")
    while True:
        pick = input("""
1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
""")
        try:
            pick = int(pick)
        except ValueError:
            print("enter a number not a string")
            continue
        if pick not in shlomi:
            print("not a valid number")
            continue
        if pick == 1:
            print()
            enable()
            print("""
-------------respect-------------
the prodoct successfully created 
where would you like to go next?""")
        if pick == 2:
            print("""
these are all the active products. 
-------------all-true-------------
""")

            print(Product_display_true())
            print("""

-------------all-true-------------
where would you like to go next?
""")

        if pick == 3:
            print(search_by_name_1())

        if pick == 4:
            print(update_meneger()
                  )
        if pick == 5:
            manager_delet()
        if pick == 6:
            break
