from function.Manager_Menu_1.Input import string, get_number, get_inventory, new_name_up, new_price_up, new_active_up
from function.Manager_Menu_1.product_creation import id_len_products, creat_produc, add_product_to_the_list
from function.Manager_Menu_1.display_all_products import despley
from function.Manager_Menu_1.product_search import search_by_name
from function.Manager_Menu_1.product_update import product_update_name, product_update_price, product_update, valid
from function.Manager_Menu_1.deleting_a_product import deleting_valid, delit
from function.Inventory_Management.Show_full_inventory import get_positive_number, show_all, search_inventory, name_for_product, add_stock, deduct_units_from_inventory, products_with_0_stock, products_with_low_stock

products = [{"id": 1, "name": "Gaming Mouse", "price": 150.0, "stock": 20, "active": True},
            {"id": 2, "name": "Mechanical Keyboard", "price": 350.0, "stock": 10, "active": True}]


def enable():
    name = string()
    price = get_number()
    inventory = get_inventory()
    id_ = id_len_products(products)
    product = creat_produc(name, price, inventory, id_)
    add_product_to_the_list(product, products)


def Product_display_true():
    products_true = despley(products)
    return products_true


def search_by_name_1():
    name = string()
    search = search_by_name(name, products)
    return search


def update_meneger():
    val = valid(products)

    while True:
        shlomi = [1, 2, 3, 4]
        print("What would you like to change?")
        pick = input("""
1.name
2.price
3.active
4.break

    """)
        try:
            pick = int(pick)
        except ValueError:
            print("enter a valid number")
            continue
        if pick not in shlomi:
            print("a number must be (1-3)")
            continue
        if pick == 1:
            new_n = new_name_up()
            product_update_name(val, new_n, products)
            print(f"""
=============================================
The product name has been changed to {new_n}
=============================================
""")

        if pick == 2:
            new_p = new_price_up()
            product_update_price(val, new_p, products)
            print(f"""
=============================================
The product price has been changed to {new_p}
=============================================
""")

        if pick == 3:
            bool_ = new_active_up()
            product_update(val, bool_, products)
            print(f"""
=============================================
The product active has been changed to {bool_}
=============================================
""")

        if pick == 4:
            break


def manager_delet():
    number_id = deleting_valid(products)
    delit(number_id, products)


def inventory_show_all():
    show_all(products)


def inventory_search():
    name = name_for_product()
    return search_inventory(name, products)


def inventory_add_stock():
    name = name_for_product()
    add_stock(name, products)


def inventory_deduct_stock():
    name = name_for_product()
    deduct_units_from_inventory(name, products)


def inventory_out_of_stock():
    products_with_0_stock(products)


def inventory_low_stock():
    threshold = get_positive_number("enter the low stock threshold: ")
    products_with_low_stock(products, threshold)
