def add(x , y):
    return(x + y)

def sub(x , y):
    return(x - y)

def multiply(x , y):
    return (x * y)

def divide(x , y):
    return (x / y)


while True:
    print("hey, please choose an operation")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choose = input("choose any of the operations 1, 2, 3, 4: ")
    try:
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
    except ValueError:
        print("please enter a valid number")

        continue

    if choose == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    
    elif choose == "2":
        print(num1, "-", num2, "=", sub(num1, num2))
    
    elif choose == "3":
        print(num1, "x", num2, "=", multiply(num1, num2))

    elif choose == "4":
        print(num1,"/", num2, "=", divide(num1, num2))


    next = input("do you want to do another calculation: yes, no")
    if next == "no":
        break
else:
    print("invalid input lodu")

