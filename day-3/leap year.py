year=int(input("which year do you want to check?: "))
if year % 4 == 0:
    if year%100 == 0:
        if year % 400 == 0: 
            print(f"{year} is Leap Year!")
        else:
            print(f"{year} is Non Leap Year!!")
    else:
         print(f"{year} is Leap Year")
else:
    print(f"{year} is Not Leap Year")