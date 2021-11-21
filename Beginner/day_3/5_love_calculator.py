# Program that tests the compatibility between two people.
#   To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

counter_true = name1.count('t') + name2.count('t') + name1.count('r') + name2.count('r') + name1.count('u') + name2.count('u') + name1.count('e') + name2.count('e')

counter_love = name1.count('l') + name2.count('l') + name1.count('o') + name2.count('o') + name1.count('v') + name2.count('v') + name1.count('e') + name2.count('e')

total = str(counter_true) + str(counter_love)
total_counter = int(total)

if total_counter < 10 or total_counter > 90:
  print(f'Your score is {total}, you go together like coke and mentos.')
elif total_counter >= 40 and total_counter <= 50:
  print(f'Your score is {total}, you are alright together.')
else:
  print(f'Your score is {total}')
