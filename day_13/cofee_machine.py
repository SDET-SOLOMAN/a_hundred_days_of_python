from arts.day_13 import MENU, resources

TOTAL_SALE = 0


def resource_checker(user_input):
    for k, v in MENU[user_input]['ingredients'].items():
        if resources[k] < v:
            print(f"Sorry there is not enough {k}.")
            return False
    return True


def minus_resource(boolean_, user):
    if boolean_:
        for k, v in MENU[user]['ingredients'].items():
            resources[k] -= v


def money(quarters, dimes, nickels, pennies, user_input):
    global TOTAL_SALE

    total_inserted = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)
    total_cost = MENU[user_input]['cost']

    if total_inserted >= total_cost:
        TOTAL_SALE += total_cost
        change = total_inserted - total_cost
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {user_input} ☕️. Enjoy!")
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def report():
    for k, v in resources.items():
        print(f"{k}:{v}")


def make_coffee():

    user = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if user == 'report':
        report()
    elif user == 'exit':
        exit()
    else:
        if MENU.get(user):
            if resource_checker(user):
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickels = int(input("how many nickels?: "))
                pennies = int(input("how many pennies?: "))
                minus_resource(money(quarters, dimes, nickels, pennies, user), user)
        else:
            print("That's not a valid selection")
    make_coffee()


make_coffee()
