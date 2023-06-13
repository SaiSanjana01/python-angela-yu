#FUNCTIONS WITH OUTPUT

def my_name(first,last):
    #DOCSTRING
    """ It will take the first and last name ad format it
    to return the title case version of the code!"""
    ff=first.title()
    fl=last.title()

    #This function terminates the other functions if there is an empty string
    if ff== "" or fl== "":
        """ IT RETURNS IF THERE IS NO FIRST AND LAST NAME! """
        return "get lost u didnn't type any name!"
    #this code below replaces the part of the code when calling the function
    return f"{ff} is my first name and my last name is {fl}"


print(my_name(input("what is your first name?: "),input("what is your last name")))
#It'll explain the code that what itll do :)
#my_name()