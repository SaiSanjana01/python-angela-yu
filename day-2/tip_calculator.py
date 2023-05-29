print("Welcome to the tip calculator!")
bill_amount=float(input("What is the total bill amount?:$ ")) 
tip_percentage=int(input("What percentage tip would you like to give $10, $12 or $15?: "))
number_of_people=int(input("How many people are going to split the bill?: "))
total_tip_percentage= float(tip_percentage/100)
sum_value = bill_amount * total_tip_percentage
total_bill_percentage = bill_amount + sum_value
total_bill_amount_split= total_bill_percentage/number_of_people
rounded_value=round(total_bill_amount_split,2)
print(f"Each person should pay: {rounded_value}")
