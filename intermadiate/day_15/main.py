from art import logo
from art import cups
import os
from data_coffe import MENU
from data_coffe import resources
import time
from art import cups_user

os.system("clear")


def drink_printer(user_drink, money):
    print(f"\nPreparing your {user_drink}.")
    time.sleep(3.5)
    print(f"\nYour {user_drink} is ready.")
    print(cups_user[user_drink])
    print(f"Your change is: ${money - MENU[user_drink]['cost']}")


def resources_checker(user_choice, money):
    if money >= MENU[user_choice]['cost']:
        if user_choice == 'espresso':
            if resources['water'] >= MENU[user_choice]['ingredients']['water']:
                if resources['coffee'] >= MENU[user_choice]['ingredients']['coffee']:
                    resources['water'] -= MENU[user_choice]['ingredients']['water']
                    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                    resources['money'] += MENU[user_choice]['cost']
                    return drink_printer(user_choice, money)
                else:
                    return print("Sorry, no enough coffee.")
            else:
                return print("Sorry, not enough water.")
        elif user_choice == 'latte' or user_choice == 'cappuccino':
            if resources['water'] >= MENU[user_choice]['ingredients']['water']:
                if resources['milk'] >= MENU[user_choice]['ingredients']['milk']:
                    if resources['coffee'] >= MENU[user_choice]['ingredients']['coffee']:
                        resources['water'] -= MENU[user_choice]['ingredients']['water']
                        resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                        resources['milk'] -= MENU[user_choice]['ingredients']['milk']
                        resources['money'] += MENU[user_choice]['cost']
                        return drink_printer(user_choice, money)
                    else:
                        return print("Sorry, not enough coffee.")
                else:
                    return print("Sorry, not enough milk")
            else:
                return print("Sorry, not enough water.")
        else:
            return print("Sorry invalid input.")
    else:
        return print("sorry that's not enough money. Money refunded.")


def start():  # main function
    exit = False

    print(logo)
    print(cups)

    while not exit:

        user_drink_selected = input("What would you like to drink? 'espresso', 'latte' or 'cappuccino': ").lower()

        if user_drink_selected == 'report':
            print(resources)
            continue
        elif user_drink_selected == 'off':
            quit()

        print("Please insert coins.")

        quarters = float(input("How many quarters?: ")) * 0.5
        dimes = float(input("How many dimes?: ")) * 0.1
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01

        total_user_money = round(quarters + dimes + nickles + pennies, 2)
        print(f"\nTotal money: {total_user_money}")
        time.sleep(2.5)

        resources_checker(user_drink_selected, total_user_money)

        enter_to_continue = input("\nPress Enter key to continue...")

        os.system("clear")
        print(logo)
        print(cups)
        

start()


