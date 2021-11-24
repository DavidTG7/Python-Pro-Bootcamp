# Rock, paper, scissors game!

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print(type(player))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print('Invalid option, GAME OVER!')
  exit()

print('\nMachine election:')
machine = random.randint(0, 2)

if machine == 0:
  print(rock)
elif machine == 1:
  print(paper)
elif machine == 2:
  print(scissors)

if player == machine:
  print('It\'s a DRAW!')
elif player == 0 and machine == 2:
  print('You WIN!')
elif player == 0 and machine == 1:
  print('Machine WINS!')
elif player == 1 and machine == 0:
  print('You WIN!')
elif player == 1 and machine == 2:
  print('Machine WINS!')
elif player == 2 and machine == 0:
  print('Machine WINS')
else:
  print('You WIN!')

