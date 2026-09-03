

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




def calc(func,num1,num2):
    ops = "+-/*"
    print(eval(f"{num1}{ops[func-1]}{num2}"))
f = "try again"
aeiou = f
func = False
while func not in [1,2,3,4]:
    while True:
        
        try:
            func = int(input("""
1 for addition\n2 for subtraction\n3 for division\n4 for multiplication\n"""))
            break
        except Exception as e:
            print(aeiou)
            continue
num1 = float(input("please give yer first number"))
num2 = float(input("please give yer sec'nd numb'r"))

calc(func,num1,num2)

