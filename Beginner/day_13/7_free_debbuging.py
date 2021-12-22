############DEBUGGING#####################

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

""" For this peaced of code I've found one mistake, in the 3rd line the if condition is evaluating
but the operator is wrong, instead of = operator it has to be ==."""

# Debbuged:
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


