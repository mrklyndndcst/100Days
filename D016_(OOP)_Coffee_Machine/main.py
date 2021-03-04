from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine = True
while machine:
    choices = input(f"What would you like? {menu.get_items()}").lower()
    if choices == "off":
        machine = False
    elif choices == "report":
        coffee_maker.report()
        money_machine.report()
    elif choices == 'latte' or choices == 'espresso' or choices == 'cappuccino':
        drink = menu.find_drink(choices)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print(f"We only serve {menu.get_items()} here.")