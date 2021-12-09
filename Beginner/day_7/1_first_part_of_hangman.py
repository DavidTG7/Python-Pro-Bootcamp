import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word_num = random.randint(0, len(word_list) - 1)
chosen_word = word_list[chosen_word_num]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter: ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word = []
for n in chosen_word:
  word += '_'
for n in range(0, len(chosen_word)):
  if guess == chosen_word[n]:
    word[n] = guess[0]

print(word)


# Angela's solution to part 3:

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

