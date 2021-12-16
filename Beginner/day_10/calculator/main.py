from art import logo
import os

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

print(logo)
num1 = float(input("What's the first number?: "))


def final_operation(operator_symbol):
  return operations[operator_symbol](num1, num2)

again = 'y'

while again == 'y':
  if again == 'y':
    for operator in operations:
      print(operator)
    operator_symbol = input("Pick an operation: ")
    num2 = float(input("What's your next number?: "))
    answer = final_operation(operator_symbol)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    num1 = answer
  again = input(f"Type 'y' to keep calculating with {answer}, or type 'n' to exit: ").lower()
