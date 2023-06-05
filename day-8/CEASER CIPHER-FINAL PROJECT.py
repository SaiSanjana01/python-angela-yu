
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(st,shift_amount,cd):
    cipher_text=""
    if cd == "d":
            shift_amount *= -1
    for char in st: 
        if char in alphabet:
            position= alphabet.index(char)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
             cipher_text += char

    print(f"the {cd}d text is {cipher_text}")

from art import logo
print(logo)

continues=True
while continues:

    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    os.system('cls')
    #if the user enter a shift greater than the number of letters
    shift%=25

    ceaser(st=text,shift_amount=shift,cd=direction)

    result=input("Type 'y' to continue or Type 'n' to exit the loop")
    if result=="n":
         continues=False
         print("Goodbye!")

