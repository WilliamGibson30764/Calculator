import pygame
import random
import time
from random import randint

#Asking for values
first = int(input("What is the first value?\n"))
second = int(input("What is the second value?\n"))
symbol = input("What do you want the sign to be?\n")
true = "True"

while true == "True":
    if symbol == "multiply":
        end = (first*second)
        true = "False"
    elif symbol == "divide":
        order = input("Which number do you want to go first(first, second)?\n")
        if order == "first":
            end = (first/second)
            true = "False"
        elif order == "second":
            end = (second/first)
            true = "False"
    elif symbol == "add":
        end = (first + second)
        true = "False"
    elif symbol == "subtract":
        order = input("Which number do you want to go first(first, second)?\n")
        if order == "first":
            end = (first - second)
            true = "False"
        elif order == "second":
            end = (second - first)
            true = "False"
    else:
        symbol = input("What do you want the sign to be?\n")
        true = "True"
print(end)