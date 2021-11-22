# Program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8.

two_digit_number = input("Type a two digit number: ")

num_char = str(two_digit_number)
a = int(num_char[0])
b = int(num_char[1])
print(a + b)
