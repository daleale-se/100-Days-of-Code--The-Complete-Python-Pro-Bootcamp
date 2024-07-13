from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True

    while is_on:
        drinks = menu.get_items()[:-1]
        choice = input(f"What would you like? ({drinks}): ")
        drink = menu.find_drink(choice)
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            is_on = False
        elif drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

    return 0


main()
