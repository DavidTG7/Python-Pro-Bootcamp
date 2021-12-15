# Program challenge: blind auction using dictionaries and choosing the highest bidder.

import os
from art import logo
print(logo)

users = {}

def max_bidder(bidders):
  max_bid = 0
  for bidder in bidders:
    actual_amount = bidders[bidder]
    if actual_amount > max_bid:
      max_bid = actual_amount
      winner = bidder
  print(f"The winner of the blind auction is {winner.upper()}, with a bid of ${max_bid}.\n")


def auction_users():
  again = 'yes'
  while again == 'yes':
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    again = input("Are there any other bidder? Type 'yes' or 'no': ").lower()
    users[name] = bid
    os.system("clear")
  max_bidder(bidders = users)

auction_users()

