def Calculator(number1,number2,operator):
    if operator == "+":
        result= Addition(number1,number2)
        DisplayResult(number1,number2,operator,result)
    elif operator == "-":
        result= Subtraction(number1,number2)
        DisplayResult(number1,number2,operator,result)
    elif operator == "*":
        result= Multiplication(number1,number2)
        DisplayResult(number1,number2,operator,result)
    elif operator == "/":
        result= Division(number1,number2)
        DisplayResult(number1,number2,operator,result)
    else:
        print("Invalid operator")

def Addition(number1,number2):
    return number1 + number2

def Subtraction(number1,number2):
    return number1 - number2

def Multiplication(number1,number2):
    return number1 * number2

def Division(number1,number2):
    return number1 / number2

def DisplayResult(number1,number2,operator,result):
    print(F"{number1} {operator} {number2} = {result}")
    
    
if __name__=="__main__":
    number1=float(input("Enter first number: "))
    operator=str(input("Enter the operator (+, -, *, /): "))
    number2=float(input("Enter second number: "))

    
    Calculator(number1,number2,operator)