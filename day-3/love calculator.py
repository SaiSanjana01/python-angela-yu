print("Welcome to love calculator!")
name1 = input("What is your name? \n")
name2 = input("what is their name? \n")
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

combined_name=lower_case_name1 + lower_case_name2

t=combined_name.count("t")
r=combined_name.count("r")
u=combined_name.count("u")
e=combined_name.count("e")

true_count=t+r+u+e

l=combined_name.count("l")
o=combined_name.count("o")
v=combined_name.count("v")
e=combined_name.count("e")

love_count= l+o+v+e

love_score = str(true_count)+ str(love_count)
love_score_int=int(love_score)

if love_score_int < 10 or love_score_int > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos!")
elif love_score_int >=40 and love_score_int <=50:
    print(f"Your score is {love_score}, you are alriight together!")
else:
    print(f"Your score is {love_score}")
