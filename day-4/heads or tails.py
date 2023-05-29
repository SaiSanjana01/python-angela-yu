import random

#for the numbers to be stable we use seed fn.!
test_seed=int(input("create a seed number: "))
random.seed(test_seed)
rand_num=random.randint(0,1)
if rand_num == 1:
    print("Heads")
else:
    print("Tails")
