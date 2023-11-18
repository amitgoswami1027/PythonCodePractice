lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'éncode' to encrypt , type 'decrypt' to decrypt")
text = input ("Type your answer").lower()
shift = int(input("Type shift number"))

#TODO : Create a function call encrypt that can take text and shift as inputs.

def encrypt (plain_text, shift_amount):
    