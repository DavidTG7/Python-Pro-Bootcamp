# Part one of the challenge Caesar Cipher, it generates an error if user input a larger shift than the lenght of the alphabet list, it will be fixed in next parts.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encrypted += new_letter
    print(encrypted)
  

encrypt(text, shift)

