#ADDITION
def add(n1,n2):
    return n1 + n2

#SUBTRACTION
def sub(n1,n2):
    return n1 - n2

#MULTIPLICATION
def mul(n1,n2):
    return n1 * n2

#DIVISION
def div(n1,n2):
    return n1 / n2

#TO CALL THESE FUNCTIONS
operators={"+":"add",
     "-":"sub",
     "*":"mul",
     "/":"div"}

#Create the numbers of first and second
n1=int(input("What is the first number? "))
n2=int(input("What is the second number? "))

#TO loop through the dictionary to access the symbols

for op in operators:
    print(op)
op_symbol = input("Pick an operation from the line above: ")

calc_function = operators[op_symbol]
answer = calc_function(n1,n2)


print(f"{n1} {op_symbol} {n2} = {answer}")