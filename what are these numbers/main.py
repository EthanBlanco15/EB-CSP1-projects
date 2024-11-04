#Ethan Blanco, ProficiencyTest: What are these numbers?

num = input("What is your number?")
num = int(num)
thousands = "Your number placed in the thousands is {:,}"
print(thousands.format(num))
Float = "Your number placed as a float is {:f}"
print(Float.format(num))
percentage = "Your number placed as a percentage is {:%}"
print(percentage.format(num))
dollar = "Your number placed as a dollar value is {:.2f}"
print(dollar.format(num))