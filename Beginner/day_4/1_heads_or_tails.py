# Virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

coin = random.randint(0, 1)

if coin == 1:
  print('Heads')
else:
  print('Tails')
