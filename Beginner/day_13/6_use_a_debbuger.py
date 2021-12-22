############DEBUGGING#####################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

""" Using pythontutor I could realize that there is an error in the function scope, in 5th line
We can see that the b_list.append(new_item) is indented as an element in the global scope of the 
function, so, it is going to add just the last value after the for loop while we want to add the
value multiplyed for 2 for each valu of the list, this way, this line has to be indented inside the
for scope."""

# Debbuged:
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
