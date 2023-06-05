alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: create a function called 'encrypt' that takes 'text' and 'shift' as inputs
def encrypt(text_letter,shift_amount):
    et=""# to print it as a string
    for ar in text_letter:
        position= alphabet.index(ar)
        new_position = position + shift_amount
        new_letter= alphabet[new_position]
        et += new_letter
    print(f"the encoded text is {et}")
# TODO-2: inside the encrypt function.shift each letter of the 'text' and 'shift' as inputs.

# TODO-3 call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text_letter= text, shift_amount= shift)
