import random
import os
 
#task-1 => to randomly choose a word 
from hangman_words import word_list
choosen_word=random.choice(word_list)

#task-8 => create a variable called lives to keep track of the number of lives left
lives=6 

# import the logo here!
from hangman_art import logo,stages
print(logo)

print(f'psst, the solution is {choosen_word}')

#task-4 create an empty list and for each letter in chosen_word , add a "_" to display

display=[]
for letters in choosen_word:
    display+= "_"

#task-7 => use a while loop to let the user guess again. the loop should stop once the user has guessed all the letters from the chosen_word and display has more blanks

end_of_game=False
while not end_of_game:
#task-2 => to ask the user to guess the letter
    guess=input('guess a letter  ').lower()

    # Clearing the Screen
    os.system('cls')
    
    #task-11 => if the user has entered a letter they've already guessed , print the letter and let them know
    if guess in display:
        print(f"already guessed the letter {guess}")

    #task-5 loop through the position in chosen_word if letter at the position matches "guess" then reveal the letter
    #task-3 => to check if the letter the user guessed is in chosen_word

    for position in range(len(choosen_word)):
        i = choosen_word[position]
        print(f"current position: {position}\n current letter:{i}\n guessed letter:{guess}")
        if i ==  guess:
            display[position] = i

    #task-8 => if guess is not in letter in chosen_word,
    #the life will reduce by 1.if lives goes down to 0 then the game should stop and it should print "You lose!"

    if guess not in choosen_word:
        
        #task-12 => If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(f"you guessed the letter {guess} that's not in the word. You lose a life")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("you lose!")
    

    #task-6 print display
    #join all the elements in the list and turn it into string
    print(f"{''.join(display)}") #since it is a list we are using join to form a string

    if "_" not in display:
        end_of_game = True
        print("You win!")

    #task-10 => print the ascii art from stages that corresponds to the current number of lives the user has remaining
    #from hangman_art import stages
    print(stages[lives])

