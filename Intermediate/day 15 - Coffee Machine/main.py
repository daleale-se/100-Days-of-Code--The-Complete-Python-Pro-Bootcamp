import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: If there is enough resources prompt the user to insert coins, quarters = $0.25,
#   dimes = $0.10, nickles = $0.05, pennies = $0.01.
QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKLE_VALUE = 0.05
PENNY_VALUE = 0.01


def clear():
    os.environ['TERM'] = 'xterm'
    os.system('clear')


def check_resources(drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calc_amount():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickles * NICKLE_VALUE + pennies * PENNY_VALUE


def use_resources(drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]


def coffee_machine():
    is_on = True
    profit = 0
    while is_on:
        clear()
        # TODO: Prompt user by asking "What would you like? (espresso/latte/cappuccino):".
        action = input("What would you like? (espresso/latte/cappuccino): ")

        if action in ["espresso", "latte", "cappuccino"]:
            drink = MENU[action]
            # TODO: Check resources to make the drink. If is not enough resources print "Sorry there is not enough {
            #   resource}."
            if check_resources(drink["ingredients"]):
                amount = calc_amount()
                # TODO: Check transaction successful, contemplate if the user insert not enough money ("Sorry that's
                #   not enough money. Money refunded."), the exact amount or if the user has inserted too much money
                #   (“Here is ${change} dollars in change.")
                if amount >= drink["cost"]:
                    if amount > drink["cost"]:
                        change = amount - drink["cost"]
                        print("Here is ${:0.2f} dollars in change.".format(change))
                    # TODO: Making a drink deduct ingredients from the Coffee Machine resource.
                    profit += drink["cost"]
                    use_resources(drink["ingredients"])
                    # TODO: When the drink is ready tell user "Here is your {drink}. Enjoy!"
                    print(f"Here is your {action}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        # TODO: Print a report with the current resource values when user enters "report".
        elif action == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {profit}")
        # TODO: Turn off the Coffee Machine by entering "off" to the prompt.
        elif action == "off":
            is_on = False


def main():
    coffee_machine()
    return 0


main()
