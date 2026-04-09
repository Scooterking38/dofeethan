#print with upper lower included and variables COncatenashun
ethan = "amazing"
lesser = "ELIJAH"
print("ethan is",ethan.upper(),"just like "+lesser.lower(),"isn't")

#numbers and if ese
number = 999999999999999999999999999999999999999999999999999999999999999999999
if number <= 3648284927448294:
    print("lalalalalalalalalallalala")
else: print("scream")

#basic calc already
print("welcome to cslc short for cslculator")
option = int(input("enter 1 for +\nenter 2 for -\nenter 3 for /\nenter 4 for *\nGIMME NUMNUM: "))
num1 = int(input("what be number of di first: "))
num2 = int(input("give me yer two'th number: "))
print("ta da. here be it. di ansuh o' t' kweschin is:")
if option == 1: 
    print(num1+num2)
elif option == 2:
    print(num1-num2)
elif option == 3:
    print(num1/num2)
elif option == 4:
    print(num1*num2)
else:
    print("u poopoo hed")

#swapping if else for match
print("welcome to cslc short for cslculator")
option = int(input("enter 1 for +\nenter 2 for -\nenter 3 for /\nenter 4 for *\nGIMME NUMNUM: "))
num1 = int(input("what be number of di first: "))
num2 = int(input("give me yer two'th number: "))
print("ta da. here be it. di ansuh o' t' kweschin is:")
match option: 
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1/num2)
    case 4:
        print(num1*num2)
    case _:
        print("gimme a reason not to cry")
