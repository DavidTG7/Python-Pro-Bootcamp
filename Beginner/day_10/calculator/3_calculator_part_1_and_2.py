# Solution to Calculator Challenge, part 1 and 2:

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

num1 = int(input("What's the first number?: "))

for operator in operations:
  print(operator)

operator_symbol = input("Pick an operation from the list above: ")

num2 = int(input("What's the second number?: "))


def final_operation(operator_symbol):
  return operations[operator_symbol](num1, num2)

answer = final_operation(operator_symbol)

print(f"{num1} {operator_symbol} {num2} = {answer}")

again = 'y'

while again == 'y':
  again = input(f"Type 'y' to keep calculating with {answer}, or type 'n' to exit: ").lower()
  if again == 'y':
    num1 = answer
    operator_symbol = input("Pick an operation: ")
    num2 = int(input("What's your new number?: "))
    answer = final_operation(operator_symbol)
    print(f"{num1} {operator_symbol} {num2} = {answer}")

