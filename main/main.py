from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

off=False

coffeeMaker=CoffeeMaker()
menu = Menu()
money = MoneyMachine()



while not off:
    ans= input(f"What would you like? {menu.get_items()}: ")
    if ans == 'off':
        off= True 
    elif ans =='report':
        coffeeMaker.report()
    else:
        item = menu.find_drink(ans)
        if coffeeMaker.is_resource_sufficient(item):
            print(f"a {item.name} will be {item.cost}")
            paid = money.make_payment(item.cost)
            if paid == True:
                coffeeMaker.make_coffee(item)
            else:
                print("I'm sorry that's not enough money ")
        else:
            print("I'm sorry we don't have enough of the ingredents to make that")
            











""" from turtle import Turtle, Screen 
timmy = Turtle()
timmy.shape('turtle')
timmy.color('DeepPink')
print(timmy)
timmy.forward(200)

my_screen=Screen()
my_screen.exitonclick """
""" 
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon name",["pikachu","squirtle","charmander"])
table.add_column("pokemon type",["electric","water","fire"])

print(table) """