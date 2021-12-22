############DEBUGGING#####################

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year = 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

"""Here I can see a promblem with the if and elif conditions, they are evaluating range of years
but omiting the 1994 year, the if condition is evaluating a reange between 1980 and 1994 and
because it is using only the < 1994, this year is not included in the evaluation of the condition
and in the elif part it says > 1994 which is not including that year either, thus, if we put as input the 1994 year nothing is going to happen even when we are typing a valid year for both ranges."""

# Debbuged:
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
