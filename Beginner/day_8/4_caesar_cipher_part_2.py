# Part one of the challenge Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % len(alphabet)

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    if new_position > len(alphabet) - 1:
        new_position -= len(alphabet)
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    decoded = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position > len(alphabet) - 1:
            new_position -= len(alphabet)
        decoded += alphabet[new_position]
    print(f"The decoded text is: {decoded}")



if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(text, shift)

