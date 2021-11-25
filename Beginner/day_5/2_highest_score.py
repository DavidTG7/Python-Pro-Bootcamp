# Program that calculates the highest score from a List of scores.

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_val = student_scores[0]
counter = 0

for max_ in student_scores:
  if max_val < student_scores[counter]:
    max_val = student_scores[counter]
  counter += 1

print(f'The highest score in the class is: {max_val}')

