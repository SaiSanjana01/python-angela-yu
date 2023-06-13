import random
from art3 import logo

to_play =True
while to_play:
    want_play=input("Do you want to play blackjack? Type 'y' or 'n': ")
    if want_play == 'y':
        print(logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        choices = random.randint(2,11)
        user_choices = random.sample(cards,2)

        # To sum up the numbers first
        start = 0
        for numbers in user_choices:
            start += numbers
        #print(start)
        #print(choices)
        print(f"Your cards: {user_choices} , current score is: {start}")

        #TO frame other calculation for the computer]
        end=0
        computer_choice = random.sample(cards,2)
        for numbers in computer_choice:
            end += numbers
        # print(end)
        print(f"for my reference the computer choice is:{computer_choice}")
        print(f"computer's first cards {computer_choice[0]},  current score is: {end}")

        another_card= False
        while not another_card:
            card=input("Type 'y' to get another card, type 'n' to pass: ")
            if card == 'y':
                user_choices.append(choices)
                print(f"The choice list of the user after the append is {user_choices}")
                start = sum(user_choices)
                print(start)
                if start > 21:
                    print("Bust! Your hand value exceeds 21. You lose!")

                if start < 21:
                    computer_choice.append(choices)
                    print(f"The choice list of the computer after the append is {computer_choice}")
                    end = sum(computer_choice)
                    print(end)
                if start > 21:
                    print("You lose!")
                elif end > 21:
                    print("Computer busts! You win!")
                elif start == end:
                    print("It's a tie!")
                if start > end:
                    print("You win!")
                else:
                    print("You lose!")
                break
            else:
                another_card = True
                if start > end:
                    print("You win!")
                else:
                    print("You lose!")
    else:
        to_play= False
