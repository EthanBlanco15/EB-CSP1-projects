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
        print(num1 + num2)
        print(num1 - num2)
        print(num1 * num2)
        print(num1 / num2)
        print(num1 ** num2)
        print(num1 // num2)
        print(num1 % num2)
    except:
        if num2 ==0:
            print("This doesn't work properly.")
            continue