# A program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

lenght_name = len(names)

who_pay = random.randint(0, lenght_name-1)

print(f'{names[who_pay]} is going to buy the meal today!')

