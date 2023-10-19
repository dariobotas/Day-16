"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

#import turtle
#from turtle import Turtle, Screen
#from prettytable import PrettyTable

#tinny = turtle.Turtle()
#my_screen = turtle.Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()
"""for c in ['red', 'green', 'blue', 'yellow']:
    tinny.color(c)
    tinny.forward(75)
    tinny.left(90)"""

#table = PrettyTable()
#table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander","Meotwo"])
#table.add_column("Type", ["Electric","Water","Fire","Psyche"])

#table.align = "l"

#print(table)
"""
Coffe machine - main.py
"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu_machine = Menu()

is_on: bool = True

while is_on:
  drink_ask = input(
    f"What would you like? ({menu_machine.get_items()}): ").lower()
  #menu_machine.menu()
  if drink_ask == "off":
    is_on = False
  elif drink_ask == "report":
    coffee_machine.report()
    money_machine.report()
  else:
    drink = menu_machine.find_drink(drink_ask)
    if coffee_machine.is_resource_sufficient(
        drink) and money_machine.make_payment(drink.cost):
      coffee_machine.make_coffee(drink)
