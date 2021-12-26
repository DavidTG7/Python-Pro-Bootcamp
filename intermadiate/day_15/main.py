from art import logo
from art import cups
import os
from data_coffe import MENU
from data_coffe import resources

os.system("clear")

print(MENU['latte']['ingredients']['water'])


def resources_checker(user_choice, money):
    if money >= MENU[user_choice]['cost']:
        print(resources)
        if user_choice == 'espresso':
            if resources['water'] >= MENU[user_choice]['ingredients']['water']:
                if resources['coffee'] >= MENU[user_choice]['ingredients']['coffee']:
                    resources['water'] -= MENU[user_choice]['ingredients']['water']
                    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                    print(resources)
                    return print("Preparing your drink!")
                else:
                    return print("Sorry, no enough coffee.")
            else:
                return print("Sorry not enough water.")
        elif user_choice == 'latte' or user_choice == 'capuccino':
            if resources['water'] >= MENU[user_choice]['ingredients']['water']:
                if resources['milk'] >= MENU[user_choice]['ingredients']['milk']:
                    if resources['coffee'] >= MENU[user_choice]['ingredients']['coffee']:
                        return print("Preparing your drink!")
                    else:
                        return print("Sorry not enough coffee.")
                else:
                    return print("Sorry not enough milk")
        else:
            return print("Sorry invalid input.")
    else:
        return print("sorry that's not enough money. Money refunded.")


# def drink_preparation(user_drink):

    # if user_drink == 'latte':
    #
    # elif user_drink_selected == 'espresso':
    # # something
    # elif user_drink_selected == 'capuccino':


# something
def start():  # main function
    exit = False

    while not exit:
        print(logo)
        print(cups)

        user_drink_selected = input("What would you like to drink? 'espresso', 'latte' or 'capuccino': ").lower()
        print("Pleas insert coins.")

        quarters = float(input("How many quarters?: ")) * 0.5
        dimes = float(input("How many dimes?: ")) * 0.1
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01

        total_user_money = round(quarters + dimes + nickles + pennies, 2)
        print(f"\nTotal money: {total_user_money}")

        resources_checker(user_drink_selected, total_user_money)
        # if user_drink_selected == 'latte':
        #     #something
        # elif user_drink_selected == 'espresso':
        #     # something
        # elif user_drink_selected == 'capuccino':
        #     #something


start()


