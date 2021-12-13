alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % len(alphabet)
        caesar(text, shift, direction)
    else: 
        print("Invalid option, try again: ")
        cipher()
    

def caesar(plain_text, shift_amount, direction):
    cipher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            new_char = letter 
        else:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift_amount
            elif direction == 'decode':
                new_position = position - shift_amount
            if new_position > len(alphabet) - 1:
                new_position -= len(alphabet)
            new_char = alphabet[new_position]
        cipher_text += new_char

    print(f"Here's is the {direction}d result: {cipher_text}")

    continuation = input("Type 'yes' to go again or type 'no' to end: ").lower()
    if continuation == 'yes':
        cipher()
    else:
        print("Goodbye!")
        
from art import logo

print(logo)
cipher()

