# Basic program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
