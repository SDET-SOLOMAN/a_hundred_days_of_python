from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()


def coffee_machine():
    user = input(f"What would you like? {menu.get_items()}:\n").lower()

    if user == 'report':
        money.report()
        coffee.report()

    elif user == 'off':
        exit()

    else:
        item = menu.find_drink(user)
        if item:
            if coffee.is_resource_sufficient(item) and money.make_payment(item.cost):
                coffee.make_coffee(item)

    coffee_machine()


coffee_machine()
