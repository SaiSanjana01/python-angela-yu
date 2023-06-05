alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_letter,shift_amount):
    ct=""# to print it as a string
    for ar in text_letter:
        position= alphabet.index(ar)
        new_position = position + shift_amount
        new_letter= alphabet[new_position]
        ct += new_letter
    print(f"the encoded text is {ct}")



# Todo-1: To create a different function called decrypt that takes text and shift as inputs

def decrypt(et,s):
    #Todo-2: inside the decryt shift each letter of the text backwards in the alphabet by shift amount and print the decryted text
    dt=""
    for dtt in et:
        pos=alphabet.index(dtt)
        d_pos=pos-s
        d_letter=alphabet[d_pos]
        dt+=d_letter
    print(dt)


#Todo-3: check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.then call the correct function based on the direction variable
if direction == "e":
    encrypt(text_letter= text, shift_amount= shift)
elif direction == "d":
    decrypt(et=text,s=shift)