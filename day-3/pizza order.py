print("Welcome to python pizza deliveries!")
size= input("What size pizza do you want? S,M or L ")
add_pepparoni=input("Do you want pepparoni?Y or N ")
extra_cheese =input("Do you want extra cheese?Y or N ")

bill=0
if size == "S":
    bill=15
    if add_pepparoni == "Y":
        bill+=2
        if extra_cheese == "Y":
            bill+=1
        #else:
            #print(bill)
    #else:
        #print(bill) 
elif size == "M":
    bill=20
    if add_pepparoni == "Y":
        bill+=3
        if extra_cheese == "Y":
            bill+=1
        #else:
            #print(bill)
    #else:
        #print(bill) 
else: 
    bill=25
    if add_pepparoni == "Y":
        bill+=3
        if extra_cheese == "Y":
            bill+=1
        #else:
            #print(bill)
    #else:
        #print(bill)
print(f"your final bill is ${bill}")
    
