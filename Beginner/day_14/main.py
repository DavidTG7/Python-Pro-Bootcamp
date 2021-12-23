from game_data import data 
from random import randint

def random_index(a_index):

    b_index = randint(0, 5)

    if a_index == b_index:
        b_index = random_index(b_index)
    return b_index

correct_guesses = 0

a_index = randint(0, 5)


loser = True
while loser:
    print(f"Compare A: {data[a_index]['name']}, {data[a_index]['description']}, from {data[a_index]['country']}.")

    b_index = random_index(a_index)
    print(f"Against B: {data[b_index]['name']}, {data[b_index]['description']}, from {data[b_index]['country']}.")

    user_answer = input("Who has more followers? 'A' or 'B': ").lower()
    
    a_character_foll = data[a_index]['follower_count']
    b_character_foll = data[b_index]['follower_count']

    if a_character_foll > b_character_foll:
        more_followers = 'a'
    else:
        more_followers = 'b'

    if user_answer == more_followers:
        correct_guesses += 1
        print(f"You are right! Current score: {correct_guesses}")
    else:
        print(f"Sorry, that's wrong. Final score: {correct_guesses}")
        loser = False
    
    a_index = b_index






# ompare A: Kylie Jenner, a Reality TV personality and businesswoman 
# and Self-Made Billionaire, from United State