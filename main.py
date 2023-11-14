from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
ingredients = CoffeeMaker()
money = MoneyMachine()
available_coffee = drinks.get_items()

machine_on = True
while machine_on:
    order = input(f"What would you like to have? ({available_coffee}): ").lower()
    if order == "off":
        machine_on = False
    elif order == "report":
        ingredients.report()
        money.report()
    else:
        drink = drinks.find_drink(order)
        if drink in drinks.menu:
            enough_resources = ingredients.is_resource_sufficient(drink)
            if enough_resources:
                transaction_successful = money.make_payment(drink.cost)
                if transaction_successful:
                    ingredients.make_coffee(drink)