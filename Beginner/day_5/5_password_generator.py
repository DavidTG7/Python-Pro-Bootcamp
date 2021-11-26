#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Getting the lenght of each list:
total_letter = len(letters)
total_number = len(numbers)
total_symbols = len(symbols)

# To get the random list for letters:

# Getting a randomized index list of the letters list  with the user request lenght:
picked_letter = []
for n in range(0, nr_letters):
  picked_letter += [random.randint(0, total_letter - 1)]

# Converting the previous index list to a list of letters from the letters list:
final_list_letter = []
for n in range(0, nr_letters):
  final_list_letter += letters[picked_letter[n]]


# To get the random list for symbols:

# Getting a randomized index list of the symbols list  with the user request lenght:
picked_symbols = []
for n in range(0, nr_symbols):
  picked_symbols += [random.randint(0, total_symbols - 1)]

# Converting the previous index list to a list of symbols from the letters list:
final_list_symbols =[]
for n in range(0, nr_symbols):
  final_list_symbols += symbols[picked_symbols[n]]


# To get the random list for numbers:

# Getting a randomized index list of the numbers list  with the user request lenght:
picked_numbers = []
for n in range(0, nr_numbers):
  picked_numbers += [random.randint(0, total_number - 1)]

# Converting the previous index list to a list of numbers from the letters list:
final_list_numbers = []
for n in range(0, nr_numbers):
  final_list_numbers += numbers[picked_numbers[n]]


# To get the password with all randomized.

# Concatenate letters, symbols and numbers in a final list:
password = (final_list_letter + final_list_symbols + final_list_numbers)

#To shuffle the password list:
random.shuffle(password)

# To convert shuffled password list into a single string:
pass1 = ''
for n in password:
  pass1 += n

# Printing final password:
print(f'Your password is: {pass1}')

