############DEBUGGING#####################

# # Fix the Errors
# age = (input("How old are you?")
# if age > 18:
# print("You can drive at age {age}."

""" I can find 3 errors in this peace of code:
    1. A wrong indentation in 3rd line, it has to be indented afeter the if condition.
    2. print function is trying to print a variable whit out f string.
    3. if condition is evaluationg an int passed as string from the input. """

# Debbuged:
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

