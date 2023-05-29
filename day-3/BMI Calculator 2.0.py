height=input("enter the height in m: ")
weight=input("enter the weight in kgs: ")
float_height=float(height)
float_weight=int(weight)
bmi=round(float_weight/float_height**2)
if bmi<18.5:
    print(f"your bmi is {bmi}, you are under weight")
elif  bmi < 25:
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi <30:
    print(f"your bmi is {bmi}, you are over weight")
elif bmi < 35 :
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese")