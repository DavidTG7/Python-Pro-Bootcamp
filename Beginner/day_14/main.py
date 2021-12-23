from game_data import data 
from art import logo
from art import versus
from random import randint
import os

def random_index(a_index):

    b_index = randint(0, 49)

    if a_index == b_index:
        b_index = random_index(b_index)
    return b_index

def print_line():
        print("_______________________________________________")

correct_guesses = 0

os.system("clear")

print(logo)

print("Current socore: 0")

a_index = randint(0, 49)

loser = False
while not loser:
    print_line()

    print(f"Compare:\nA: {data[a_index]['name']}, {data[a_index]['description']}, from {data[a_index]['country']}.")
    
    print(versus)

    b_index = random_index(a_index)
    print(f"B: {data[b_index]['name']}, {data[b_index]['description']}, from {data[b_index]['country']}.")

    print_line()

    user_answer = input("\nWho has more followers? 'A' or 'B': ").lower()
    
    a_character_foll = data[a_index]['follower_count']
    b_character_foll = data[b_index]['follower_count']

    if a_character_foll > b_character_foll:
        more_followers = 'a'
    else:
        more_followers = 'b'
    
    os.system("clear")
    
    print(logo)
    
    
    
    if user_answer == more_followers:
        correct_guesses += 1
        print(f"You are right! Current score: {correct_guesses}")
    else:
        print(f"Sorry, that's wrong. Final score: {correct_guesses}\nGame Over!")
        loser = True
    
    a_index = b_index

