############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

""" The problem is that in the for loop we are calling the range function which will iterate in the range taht we passed to it
as argument, so, in this case, it will iterate in the range from 1 to 20 but not including 20, so it will iterate just until 19.
So, the conditon nested in the for loop never will be reached due to it is conditioning the i variable when it be exactly equal 
to 20 and then prtin "You got it". Then, we should fix this bug adding 1 to the 20 in the range function: range(1, 21), this way,
the nested if condition will be reached and executed. """


# Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()
