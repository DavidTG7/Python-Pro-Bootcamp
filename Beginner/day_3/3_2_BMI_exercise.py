# Program that interprets the Body Mass Index (BMI) based on a user's weight and height.

height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = weight / (height ** 2)
bmi = round(bmi)

if bmi < 18.5:
  print(f'Your BMI is {bmi}, you are underwight.')
elif bmi < 25:
  print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
  print(f'Your BMI is {bmi}, you are obese.')
else:
  print(f'Your BMI is {bmi}, you are clinically obese.')
