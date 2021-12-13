# Part 3 of the caesar cipher challenge:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % len(alphabet)

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




caesar(plain_text = text, shift_amount = shift, direction = direction)

