import random
from art import logo
from replit import clear

def start():
  clear()

  print(logo)

  difficulty = input("Welcome to the Guessing Number Game!\nChoose a difficulty level: 'easy' or 'hard': ").lower()


  total_list_numbers = []
  for num in range(1, 101):
    total_list_numbers.append(num)

  secret_number = random.choice(total_list_numbers)

  def print_attempts(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")

  def initial_user_attempts(difficulty):
      
    if difficulty == 'easy':
      attempts = 10
    elif difficulty == 'hard':
      attempts = 5
    else:
      print("Invalid input. Try again.")
    
    return attempts

  attempts = initial_user_attempts(difficulty)

  print_attempts(attempts)


  number_guessed = int(input("Now, guess a number between 1 and 100: "))

  while attempts > 0:
    if number_guessed < secret_number:
      print("Too low.")
    elif number_guessed > secret_number:
      print("Too high.")
    elif number_guessed == secret_number:
      print(f"{number_guessed} is the hidden number, you have guessed it!")
      break
    print_attempts(attempts)
    number_guessed = int(input("Guess again: "))
    attempts -= 1

    if attempts == 0:
      print("You lose. You have run out of guesses!")
      print(f"The hidden number is {secret_number}.")
  
  def user_play_again():
    play_again = input("Do you want to play again? ('y' or 'n'): ")

    if play_again == 'y':
      start()
    elif play_again == 'n':
      print("Good bye!")
      quit()
    else:
      print("Invalid input. Try again.")
      user_play_again()
    
  user_play_again()

start()



