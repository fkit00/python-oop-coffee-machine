""" from turtle import Turtle, Screen 
timmy = Turtle()
timmy.shape('turtle')
timmy.color('DeepPink')
print(timmy)
timmy.forward(200)

my_screen=Screen()
my_screen.exitonclick """

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon name",["pikachu","squirtle","charmander"])
table.add_column("pokemon type",["electric","water","fire"])

print(table)