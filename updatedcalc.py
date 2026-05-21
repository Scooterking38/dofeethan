

def calc(bum,num1,num2):
    ops = "+-/*"
    print(eval(f"{num1}{ops[bum-1]}{num2}"))


func = int(input("""
please select number based on what function you want to do.
type 1 for addition
type 2 for subtraction
type 3 for division
type 4 for multiplication
"""))
num1 = float(input("please give yer first number"))
num2 = float(input("please give yer sec'nd numb'r"))

calc(func,num1,num2)
