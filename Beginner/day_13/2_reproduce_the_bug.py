############DEBUGGING#####################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

""" In this piece of code I can find an error in the randint function which is going to iterate from 1 to 6 to choose a random
number from that range and insert it in the next line as an index of the dice_imgs list variable to be printed. Thus the error 
occurs when the randint try to pass 6 as index because in the dice_imgs doesnt exist an element which that index number, it has 
6 items but the first one starts at 0 index value, so the 6th item will be in the 5 index value. Plus, in the range from 1 to 6 in
the randint function, the 0 index item in the list is never going to be reached, therefore I gotta change the range from 0 to 5. """

# Debbuged:

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

