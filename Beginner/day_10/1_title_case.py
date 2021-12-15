# Function that converts a first name and a last name in title case:

def format_name(f_name, l_name):

  final_name = ''
  for i in range(len(f_name)):
    if i == 0:
      final_name += f_name[i].upper()
    else:
      final_name += f_name[i].lower()

  final_name += ' '
  for i in range(len(l_name)):
    if i == 0:
      final_name += l_name[i].upper()
    else:
      final_name += l_name[i].lower()
  return(final_name)

first_name = input("What's your first name?: ")
last_name = input("What's your last name?: ")

print(format_name(first_name, last_name))

