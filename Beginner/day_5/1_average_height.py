# Program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total1 = 0
counter = 0

for total in student_heights:
  total1 += total
  counter += 1

average = total1 / counter

print(f'total height = {total1}\nnumber of students = {counter}')
print(round(average))
