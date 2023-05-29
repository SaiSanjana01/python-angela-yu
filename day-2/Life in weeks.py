age=input("What is your current age?: ")
age_as_int=int(age)
year_reamining=90-age_as_int
days_remaining=year_reamining*365
week_remaining=year_reamining*52
month_remaining=year_reamining*12
print(f"You have {days_remaining} days, {week_remaining} weeks and {month_remaining} months left.")