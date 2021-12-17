# In this part of the BlackJack projecte I have created:
# start function.
# card_picker function.
# add_cards function (Basic state).
# card_printer function.
# black_jack function (Main function).
# art BlackJack module.

# Importing:
import random, time
from art import logo
from art import card_printer
import os

# Initial greeting and input to enter the game (Function):
def start():

  greet = "Hello! Are you ready to play Black Jack?"
  for i in range(len(greet)):
    print(greet[0:i], end = "\r")
    time.sleep(0.04)
  print(greet)

  ready = input("Type 'yes' to play or 'no' to exit: ").lower()

  if ready == 'yes':
    os.system("clear")
    black_jack()
  elif ready == 'no':
    bye = "Catch you later!"
    print("\nt(-_-t)")
    for i in range(len(bye)):
      print(bye[0:i], end = "\r")
      time.sleep(0.042)
    print(bye)
    quit()
  else:
    print("Invalid input, try again.")
    time.sleep(2)
    os.system("clear")
    start()

# Choose the cards ramdomly:
def card_picker():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  selected_cards = []
  selected_cards.append(random.choice(cards))
  selected_cards.append(random.choice(cards))
  return selected_cards

# Add cards (Basic state):
def add_cards(cards_list):
  total = 0
  for i in cards_list:
    total += i
  return total

# Main function:
def black_jack():
  print(logo)
  user_cards = card_picker()
  card_printer(user_cards)
  
  print(f"User socore = {add_cards(user_cards)}")
 
  pc_cards = card_picker()
  card_printer(pc_cards)
  print(f"PC score = {add_cards(pc_cards)}")
    
start()

