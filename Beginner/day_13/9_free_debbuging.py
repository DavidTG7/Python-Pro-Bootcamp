############DEBUGGING#####################

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

""" In this code I've found 4 errors:
    1. In the 2nd line the conditional should be compare with an 'and' and not an 'or', because
       if we just leave the 'or' any of the both condition is going to evaluate to true and execute
       the next line when what we want to do is that both conditions evaluate to true so the next 
       line is going to be executed correctly.
    2. After the first if condition we can find another if condition which has to be elif because 
       we are evaluating diferent options for one same thing.
    3. Another if condition after 2 if previous conditions, it has to be elif also.
    4. In the else statement, the print function is getting an index instead the number from the 
       range."""

# Debbuged:

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

