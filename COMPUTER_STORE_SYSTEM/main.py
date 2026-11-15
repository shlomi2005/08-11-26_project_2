from function.Manager_Menu_1.Products_Management_menu import products_management
from function.Inventory_Management.menu_inventory import inventory_management


def menu():
    shlomi = [1, 2, 3, 4, 5]
    print("""=================================
     COMPUTER STORE SYSTEM
=================================
""")
    while True:
        pick = input("""

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit

Choose an option:
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
            print(products_management())
        if pick == 2:
            inventory_management()
        if pick == 3:
            pass
        if pick == 4:
            pass
        if pick == 5:
            print("good bye ")
            break


if __name__ == "__main__":
    menu()
