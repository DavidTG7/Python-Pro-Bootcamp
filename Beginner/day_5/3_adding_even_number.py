# Program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100.

# Way number 1:

total = 0
for number in range(2, 101, 2):
  total += number
print(total)

# Way number 2:

total1 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total1 += number

print(total1)

