# Importing 
import random, time
from art import logo
from art import card_printer
from art import art_loser
from art import art_winner
from art import art_draw
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
  selected_card = random.choice(cards)
  return selected_card

# Add cards (Basic state):
def add_cards(cards_list):
  total = 0
  elevens = 0
  
  for a in cards_list:
    if a == 11:
        elevens += 1
  
  for i in cards_list: 
    total += i 
  if total > 21:
    while elevens > 0:
      if elevens > 0:
        total -= 10
        elevens -= 1
      if total <= 21:
        break
  return total

def initial_card_picker():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  player_cards.append(random.choice(cards))
  player_cards.append(random.choice(cards))
  return player_cards

def line():
  print("__________________________")

def user_pc_block(total_user, user_cards, total_pc, pc_cards):
  clear_logo()
  print("YOUR cards:")
  card_printer(user_cards)
  print(f"Your score is: {total_user}")
  line()
  print("PC cards:")
  card_printer(pc_cards)
  print(f"PC score: {total_pc}")
  line()

def player_winner(grand_total):
  total_user = grand_total[0]
  total_pc = grand_total[1]
  print(f"Your score is: {total_user}\nPC score is: {total_pc}")
  
  if total_user == total_pc:
    print(art_draw)
  elif total_user > total_pc or total_pc > 21:
    print(art_winner)
  elif total_user < total_pc:
    print(art_loser)
  play_again()

def play_again():
  again = input("Wanna play again? 'y' or 'n': ").lower()
  if again == 'y':
    os.system("clear")
    black_jack()
  elif again == 'n':
    print("Good bye!")
    quit()
  else:
    print("Invalid input. Try again.")
    time.sleep(2)
    play_again()
  
    
def clear_logo():
  os.system("clear")
  print(logo)


# Main function:
def black_jack():
  
  print(logo)
  print("YOUR cards:")
  user_cards  = initial_card_picker()
  if 11 in user_cards and 10 in user_cards:
    print(card_printer([user_cards[0], user_cards[1], 13]))
  else:
    card_printer(user_cards)
  print(f"Your score is: {add_cards(user_cards)}")
  line()

  pc_cards = initial_card_picker()
  print("PC cards:")
  card_printer([12, pc_cards[1]])
  line()

  isUserBlackjack = add_cards(user_cards) == 21
  isPCBlackjack = add_cards(pc_cards) == 21

  if isUserBlackjack and isPCBlackjack:
    user_pc_block(
      add_cards(user_cards),
      user_cards,
      add_cards(pc_cards),
      pc_cards
    )
    
    print(art_draw)
    play_again()
  
  elif add_cards(user_cards) == 21:
    user_pc_block(
      add_cards(user_cards),
      user_cards,
      add_cards(pc_cards),
      pc_cards
    )
  
    print(art_winner)
    play_again()
  
  turn_player = True

  while turn_player == True:
    total_user = add_cards(user_cards)
    total_pc = add_cards(pc_cards)
    

    if user_cards[0] == 11 or user_cards[1] == 11:
      if user_cards[0] == 10 or user_cards[1] == 10:
        break
    
    add_card = input("One more card?('y', 'n'): ")
    if add_card == 'n':
      user_pc_block(
        total_user,
        user_cards,
        total_pc,
        pc_cards
      )
      
      turn_player = False

    elif add_card == 'y':
      clear_logo()
      user_cards.append(card_picker())
      print("YOUR cards:")

      card_printer(user_cards)
      total_user = add_cards(user_cards)
      print(f"Your score is: {total_user}")

      if total_user > 21:
        print(art_loser)
        play_again()
       
      elif total_user == 21:
        time.sleep(1)

        user_pc_block(
          total_user,
          user_cards,
          total_pc,
          pc_cards
        )
        break

      line()
      print("PC cards:")
      card_printer([12, pc_cards[1]])
      line()

    else:
      print("Invalid input!")

      continue
  
  turn_pc = True

  while turn_pc == True:    
    time.sleep(1.7)    
    
    test = total_pc < total_user and total_pc < 21
    if test: 
      pc_cards.append(card_picker())
      total_pc = add_cards(pc_cards)
      
      user_pc_block(
        total_user,
        user_cards,
        total_pc,
        pc_cards
      )

    elif total_pc > 21:
      turn_pc = False
        
    elif total_pc == total_user and total_pc < 18:
      pc_cards.append(card_picker())
      total_pc = add_cards(pc_cards)
      
      user_pc_block(
        total_user,
        user_cards,
        total_pc,
        pc_cards
      )
    
    elif total_pc == total_user and total_pc > 17:
      turn_pc = False

    elif total_pc > total_user:
      turn_pc = False

  user_pc_total = []
  user_pc_total.append(add_cards(user_cards))
  user_pc_total.append(add_cards(pc_cards))
  
  player_winner(user_pc_total)  

    
start()
