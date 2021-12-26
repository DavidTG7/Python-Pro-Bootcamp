from art import logo
from art import cups

print(logo)
print(cups)

user_drink_selected = input("What would you like to drink? 'espresso', 'latte' or 'capuccino': ")
print("Pleas insert coins.")

quarters = float(input("How many quarters?: ")) * 0.5
dimes = float(input("How many dimes?: ")) * 0.1
nickles = float(input("How many nickles?: ")) * 0.05
pennies = float(input("How many pennies?: ")) * 0.01

total_user_money = quarters + dimes + nickles + pennies

git 
