import random

test_seed=int(input("create a seed number: "))
random.seed(test_seed)
 #split string messages
nameAsCSV = input("Give me everybody's name, separated by comma ")
names=nameAsCSV.split(", ")
print(names)

num_items = len(names)

#print(num_items)
random_name= random.randint(0,num_items - 1)
person_to_pay = names[random_name]
print(f"{person_to_pay} is going to buy the meal today!")



# method - 2
random_name = random.choice(names) # choice is used to like choose from a random product
print(f"{random_name} is going to buy the meal today!")