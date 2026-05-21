func = int(input("""welcome to calc,
please select number based on what function you want to do.
type 1 for addition
type 2 for subtraction
type 3 for division
type 4 for multiplication
"""))
num1 = int(input("please give yer first number"))
num2 = int(input("please give yer sec'nd numb'r"))
match func:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1/num2)
    case 4:
        print(num1*num2)
    case _:
        print("get a life and choose some proper numbers")
