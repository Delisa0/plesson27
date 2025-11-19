def checkIfSame(number1,numbr2):
    if((number1^number2)!=0):
        print("numbers are not equal")
    else:
        print("both numbers are equal")
number1=int(input("enter first number: "))
number2=int(input("Enter second number: "))
checkIfSame(number1,number2)