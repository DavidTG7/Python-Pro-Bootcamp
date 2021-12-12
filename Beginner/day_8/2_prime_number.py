# You need to write a function that checks whether if the number passed into it is a prime number or not.

def prime_checker(number):
  prime = True
  if number <= 1:
    prime = False
  for i in range(2, number - 1):
    if number > 1:
      if number % i == 0:
        prime = False
        break
  
  if prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = float(input("Check this number: "))
if n % 1 != 0:
  print("It's not a prime number.")
else:
  # int(n)
  prime_checker(number=int(n))
