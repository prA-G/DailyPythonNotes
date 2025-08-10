Number_1=float(input("Enter number 1 : "))
Number_2=float(input("Enter number 2 : "))
print("Opeartions for calculation are :")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
Calculation=input("Enter your operator here : ")
if Calculation=="+":
    print("Addition = ",Number_1+Number_2)
elif Calculation=="-":
    print("Subtraction = ", Number_1-Number_2)
elif Calculation=="*":
    print("Multiplication = ", Number_1*Number_2)
elif Calculation=="/":
    print("Division = ", Number_1/Number_2)
else:
    print("Invalid operator, Please Enter valid one❌")