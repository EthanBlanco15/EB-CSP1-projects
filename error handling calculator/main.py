#Ethan Blanco, ProfiencyTest: Simple Calculator
while True:
    try:
        num1 = input("Enter your first arithmetic number;")
        num1 = int(num1)
    except:
        print("Wrong input")
        continue
    try:
        num2 = input("Enter your second arithmetic number;")
        num2 = int(num2)
    except:
        print("Wrong input")
        continue

    try:
        calculator = input("""What arithmetic operator would you like to use?
            a. Addition               
            b. Subtraction               
            c. Multiplication               
            d. Division
            e. Exponention
            f. Floor division
            g. Module Operator                              
                           \n""")
        if calculator =="a":
            print(num1 + num2)
        if calculator =="b":
            print(num1 - num2)
        if calculator =="c":
            print(num1 * num2)
        if calculator =="d":
            print(num1 / num2)
        if calculator =="e":
            print(num1 ** num2)
        if calculator =="f":
            print(num1 // num2)
        if calculator =="g":
            print(num1 % num2)
    except:
        if num2 ==0:
            print("This doesn't work properly.")
            continue