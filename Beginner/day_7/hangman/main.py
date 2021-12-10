import random, hangman_art, hangman_words, time

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Import the logo from hangman_art.py and print it at the start of the game.

#Official Welcome:
for i in range(len(hangman_art.wel1)):
    print(hangman_art.wel1[0:i], end = "\r")
    time.sleep(0.032)
print(hangman_art.wel1 + '\n')

for i in range(len(hangman_art.wel2)):
    print(hangman_art.wel2[0:i], end = "\r")
    time.sleep(0.032)
print(hangman_art.wel2)

for i in range(len(hangman_art.wel3)):
    print(hangman_art.wel3[0:i], end = "\r")
    time.sleep(0.032)
print(hangman_art.wel3)
print(hangman_art.wel4)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# While loop for the main part of the game:
while not end_of_game:
    
    time.sleep(0.5)
    text = "Guess a letter: "
    
    for i in range(len(text)):
      print(text[0:i], end="\r")
      time.sleep(0.15)
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) > 1:
      single = "Please write a single character!"
      for i in range(len(single)):
        print(single[0:i], end = "\r")
        time.sleep(0.025)
      print(single)
      continue
    
    letters1 = 'abcdefghijklmnñopqrstuvwxyz'
    if guess not in letters1:
      print(f"'{guess}' is not a letter!")
      continue
    elif guess == '':
      print('You did not write anything...')
      continue
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in chosen_word and guess not in display:
      time.sleep(0.3)
      print(f"Well done, '{guess}' is in the word!")
    
    if  guess in display:
      time.sleep(0.3)
      already_guessed = "You have already guessed "
      for i in range(len(already_guessed)):
        print(already_guessed[0:i], end = "\r")
        time.sleep(0.031)
      print(already_guessed + "'" + guess + "'")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        time.sleep(0.6)
        print(f"'{guess}' is not in the word, lives remaining: {lives}")
        if lives == 0:
            end_of_game = True
            time.sleep(1)
            print(f"\nYou lose! The word was '{chosen_word}'.")
    

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        for i in range(len(hangman_art.win1)):
          print(hangman_art.win1[0:i], end = "\r")
          time.sleep(0.022)
        print(hangman_art.win1)

        for i in range(len(hangman_art.win2)):
          print(hangman_art.win2[0:i], end = "\r")
          time.sleep(0.022)
        print(hangman_art.win2)

        for i in range(len(hangman_art.win3)):
          print(hangman_art.win3[0:i], end = "\r")
          time.sleep(0.022)
        print(hangman_art.win3)

        for i in range(len(hangman_art.win4)):
          print(hangman_art.win4[0:i], end = "\r")
          time.sleep(0.022)
        print(hangman_art.win4)

        for i in range(len(hangman_art.win5)):
          print(hangman_art.win5[0:i], end = "\r")
          time.sleep(0.022)
        print(hangman_art.win5)

        for i in range(len(hangman_art.win6)):
          print(hangman_art.win6[0:i], end = "\r")
          time.sleep(0.022)
        print(hangman_art.win6)
        continue

#TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])

