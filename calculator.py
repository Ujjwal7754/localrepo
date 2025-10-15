def calculator():
    num1 = float(input("Enter the number : "))
    num2 = float(input("Enter the number: "))
    operation = input("choose the operation (+,-,*,/): ")

    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 + num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1/num2
    else:
        print("Choose the correct operation")
    print(result)

if __name__ == "__main__" :
    calculator()
    

    
    


