from Moduls.Moduls_GUI_shop.helpers import clean_screen

from json import load


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products_data.json", "r") as stock:
        info = load(stock)


