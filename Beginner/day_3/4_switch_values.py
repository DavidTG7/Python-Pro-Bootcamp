# Program that switches the values stored in the variables a and b.

a = input('a: ')
b = input('b: ')

aux = a
a = b
b = aux

print('a: ' + a)
print('b: ' + b)
